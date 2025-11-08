import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Tool } from './Tool'
import { Button } from '../ui/button'
import { Download, LogOut } from 'lucide-react'

interface DownloadToolProps {
  pdfId: string
}

export function DownloadTool({ pdfId }: DownloadToolProps) {
  const navigate = useNavigate()
  const [statusMessage, setStatusMessage] = useState<{ text: string; type: 'success' | 'error' | 'info' } | null>(null)

  const showStatus = (text: string, type: 'success' | 'error' | 'info' = 'info') => {
    setStatusMessage({ text, type })
    if (type !== 'error') {
      setTimeout(() => setStatusMessage(null), 3000)
    }
  }

  const handleExit = async () => {
    if (!confirm('Are you sure you want to exit? This will clean up temporary files.')) {
      return
    }

    try {
      showStatus('Cleaning up...', 'info')

      const response = await fetch(`/api/${pdfId}/cleanup/`, {
        method: 'POST',
      })

      if (!response.ok) {
        throw new Error('Failed to clean up')
      }

      showStatus('Cleanup complete. Redirecting...', 'success')

      setTimeout(() => {
        navigate('/')
      }, 1000)
    } catch (error) {
      showStatus(`Error during cleanup: ${error instanceof Error ? error.message : 'Unknown error'}`, 'error')
    }
  }

  return (
    <Tool title="Download & Exit">
      <div className="download-tool-content">
        <a
          href={`/api/${pdfId}/download/`}
          download
          className="download-link"
        >
          <Button className="w-full" variant="default">
            <Download size={16} className="mr-2" />
            Download PDF
          </Button>
        </a>

        <Button
          onClick={handleExit}
          className="w-full"
          variant="destructive"
        >
          <LogOut size={16} className="mr-2" />
          Exit & Clean Up
        </Button>

        {statusMessage && (
          <div className={`status-message status-${statusMessage.type}`}>
            {statusMessage.text}
          </div>
        )}
      </div>

      <style>{`
        .download-tool-content {
          display: flex;
          flex-direction: column;
          gap: 0.75rem;
        }

        .download-link {
          text-decoration: none;
        }

        .status-message {
          padding: 0.5rem;
          border-radius: 0.25rem;
          font-size: 0.875rem;
        }

        .status-success {
          background: #d1fae5;
          color: #065f46;
        }

        .status-error {
          background: #fee2e2;
          color: #991b1b;
        }

        .status-info {
          background: #dbeafe;
          color: #1e40af;
        }
      `}</style>
    </Tool>
  )
}
