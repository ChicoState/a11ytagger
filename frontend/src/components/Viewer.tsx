import { useEffect, useRef, useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'

interface PDFDataResponse {
  pdf_data_url: string
  pdf_id: string
  error?: string
}

declare global {
  interface Window {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    pdfjsLib: any
  }
}

export function Viewer() {
  const { pdfId } = useParams<{ pdfId: string }>()
  const navigate = useNavigate()
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const containerRef = useRef<HTMLDivElement>(null)
  const [pdfLoaded, setPdfLoaded] = useState(false)

  useEffect(() => {
    if (!pdfId) {
      setError('No PDF ID provided')
      setLoading(false)
      return
    }

    // Load PDF.js script
    const script = document.createElement('script')
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js'
    script.async = true
    script.onload = () => {
      setPdfLoaded(true)
    }
    script.onerror = () => {
      setError('Failed to load PDF.js library')
      setLoading(false)
    }
    document.body.appendChild(script)

    return () => {
      document.body.removeChild(script)
    }
  }, [pdfId])

  useEffect(() => {
    if (!pdfLoaded || !pdfId) return

    const fetchAndRenderPDF = async () => {
      try {
        const response = await fetch(`/api/${pdfId}/data/`)
        
        if (!response.ok) {
          if (response.status === 404) {
            setError('PDF not found. It may have expired.')
            setLoading(false)
            return
          }
          throw new Error('Failed to fetch PDF data')
        }

        const data: PDFDataResponse = await response.json()

        if (data.error) {
          setError(data.error)
          setLoading(false)
          return
        }

        // Set up PDF.js worker
        window.pdfjsLib.GlobalWorkerOptions.workerSrc = 
          'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js'

        // Load and render PDF
        const pdf = await window.pdfjsLib.getDocument(data.pdf_data_url).promise
        const container = containerRef.current
        
        if (!container) {
          setLoading(false)
          return
        }

        // Clear container
        container.innerHTML = ''

        // Render all pages
        for (let pageNum = 1; pageNum <= pdf.numPages; pageNum++) {
          const page = await pdf.getPage(pageNum)
          const scale = 1.5
          const viewport = page.getViewport({ scale })

          const pageDiv = document.createElement('div')
          pageDiv.className = 'pdf-page'

          const canvas = document.createElement('canvas')
          const context = canvas.getContext('2d')
          
          if (!context) continue

          canvas.height = viewport.height
          canvas.width = viewport.width

          pageDiv.appendChild(canvas)
          container.appendChild(pageDiv)

          await page.render({
            canvasContext: context,
            viewport: viewport
          }).promise
        }

        setLoading(false)
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load PDF')
        setLoading(false)
      }
    }

    fetchAndRenderPDF()
  }, [pdfLoaded, pdfId])

  if (error) {
    return (
      <div className="viewer-container">
        <div className="error-message">
          <h2>Error</h2>
          <p>{error}</p>
          <button type="button" onClick={() => navigate('/upload/')} className="back-button">
            Back to Upload
          </button>
        </div>
      </div>
    )
  }

  return (
    <div className="viewer-wrapper">
      <div className="viewer-container">
        {loading && (
          <div className="loading-message">
            <p>Loading PDF...</p>
          </div>
        )}
        <div ref={containerRef} className="pdf-pages"></div>
      </div>

      <style>{`
        .viewer-wrapper {
          height: 100vh;
          overflow: hidden;
          background: #f5f5f5;
        }

        .viewer-container {
          height: 100vh;
          overflow-y: auto;
          background: #f5f5f5;
          padding: 20px;
        }

        .pdf-pages {
          max-width: 900px;
          margin: 0 auto;
        }

        .pdf-page {
          margin-bottom: 20px;
          background: white;
          box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }

        .pdf-page canvas {
          display: block;
          width: 100%;
          height: auto;
        }

        .loading-message {
          text-align: center;
          padding: 2rem;
          font-size: 1.2rem;
          color: #666;
        }

        .error-message {
          max-width: 600px;
          margin: 2rem auto;
          padding: 2rem;
          background: white;
          border-radius: 8px;
          box-shadow: 0 2px 8px rgba(0,0,0,0.1);
          text-align: center;
        }

        .error-message h2 {
          color: #c33;
          margin-bottom: 1rem;
        }

        .error-message p {
          margin-bottom: 1.5rem;
          color: #666;
        }

        .back-button {
          background-color: var(--btn-color);
          color: var(--text-color);
          padding: 10px 20px;
          border-radius: 4px;
          font-size: 16px;
          border: none;
          cursor: pointer;
          transition: background-color 0.3s;
        }

        .back-button:hover {
          background-color: var(--btn-hover-color);
        }

        .back-button:focus {
          outline: 2px solid var(--btn-focus-color);
          outline-offset: 2px;
        }
      `}</style>
    </div>
  )
}
