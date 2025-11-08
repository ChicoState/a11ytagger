import { useState } from 'react'
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

export function Upload() {
  const [isSubmitting, setIsSubmitting] = useState(false)
  const form = useForm<UploadFormData>()

  const onSubmit = async (data: UploadFormData) => {
    setIsSubmitting(true)
    
    const formData = new FormData()
    if (data.pdf_file && data.pdf_file.length > 0) {
      formData.append('pdf_file', data.pdf_file[0])
    }

    try {
      // TODO: Replace with actual API endpoint
      const response = await fetch('/api/upload/', {
        method: 'POST',
        body: formData,
      })

      if (response.ok) {
        // Handle success
        console.log('Upload successful')
      } else {
        // Handle error
        console.error('Upload failed')
      }
    } catch (error) {
      console.error('Upload error:', error)
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <div className="upload-container">
      <h1 className="text-4xl font-bold mb-6">Upload PDF for Accessibility Tagging</h1>
      
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
