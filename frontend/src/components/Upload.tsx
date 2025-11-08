import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useForm } from 'react-hook-form'
import { Button } from 'src/components/ui/button'
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from 'src/components/ui/form'
import { Input } from 'src/components/ui/input'

interface UploadFormData {
  pdf_file: FileList
}

interface UploadResponse {
  pdf_id: string
  success: boolean
  error?: string
  warnings?: string[]
}

export function Upload() {
  const navigate = useNavigate()
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [uploadError, setUploadError] = useState<string | null>(null)
  const [uploadSuccess, setUploadSuccess] = useState<string | null>(null)
  const form = useForm<UploadFormData>()

  const onSubmit = async (data: UploadFormData) => {
    setIsSubmitting(true)
    setUploadError(null)
    setUploadSuccess(null)
    
    const formData = new FormData()
    if (data.pdf_file && data.pdf_file.length > 0) {
      formData.append('pdf_file', data.pdf_file[0])
    }

    try {
      const response = await fetch('/api/upload/', {
        method: 'POST',
        body: formData,
      })

      const result: UploadResponse = await response.json()

      if (response.ok && result.success) {
        setUploadSuccess(`Upload successful! Redirecting to viewer...`)
        form.reset()
        // Navigate to viewer
        setTimeout(() => {
          navigate(`/viewer/${result.pdf_id}/`)
        }, 1000)
      } else {
        setUploadError(result.error || 'Upload failed')
      }
    } catch (error) {
      setUploadError(`Upload error: ${error instanceof Error ? error.message : 'Unknown error'}`)
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <div className="upload-container">
      <h1 className="text-4xl font-bold mb-6">Upload PDF for Accessibility Tagging</h1>
      
      {uploadError && (
        <div className="message error-message">
          <strong>Error:</strong> {uploadError}
        </div>
      )}
      
      {uploadSuccess && (
        <div className="message success-message">
          <strong>Success:</strong> {uploadSuccess}
        </div>
      )}
      
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="upload-form">
          <FormField
            control={form.control}
            name="pdf_file"
            rules={{ required: 'Please select a PDF file' }}
            render={({ field: { onChange, value, ...field } }) => (
              <FormItem>
                <FormLabel>Upload PDF:</FormLabel>
                <FormControl>
                  <Input
                    type="file"
                    accept="application/pdf"
                    onChange={(e) => onChange(e.target.files)}
                    {...field}
                  />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          
          <Button type="submit" disabled={isSubmitting} className="submit-btn">
            {isSubmitting ? 'Uploading...' : 'Upload'}
          </Button>
        </form>
      </Form>

      <style>{`
        .upload-container {
          padding: 2rem;
        }

        .upload-form {
          max-width: 500px;
        }

        .upload-form > div {
          margin-bottom: 1.5rem;
        }

        .message {
          max-width: 500px;
          padding: 1rem;
          margin-bottom: 1.5rem;
          border-radius: 4px;
          border: 1px solid;
        }

        .error-message {
          background-color: #fee;
          border-color: #fcc;
          color: #c33;
        }

        .success-message {
          background-color: #efe;
          border-color: #cfc;
          color: #3c3;
        }

        .submit-btn {
          background-color: var(--btn-color) !important;
          color: var(--text-color) !important;
          padding: 10px 20px !important;
          border-radius: 4px;
          font-size: 16px;
          transition: background-color 0.3s;
          border: none;
          cursor: pointer;
          height: auto !important;
        }

        .submit-btn:hover:not(:disabled) {
          background-color: var(--btn-hover-color) !important;
        }

        .submit-btn:focus {
          outline: 2px solid var(--btn-focus-color) !important;
          outline-offset: 2px;
          box-shadow: none !important;
        }

        .submit-btn:disabled {
          opacity: 0.6;
          cursor: not-allowed;
        }
      `}</style>
    </div>
  )
}
