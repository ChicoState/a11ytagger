import { useState } from 'react'
import { Tool } from './Tool'
import { Button } from '../ui/button'
import { Input } from '../ui/input'
import { X, ChevronLeft, ChevronRight } from 'lucide-react'

interface ImageInfo {
  id: number
  page_number: number
  width: number
  height: number
  format: string
}

interface ImageTaggerToolProps {
  pdfId: string
}

export function ImageTaggerTool({ pdfId }: ImageTaggerToolProps) {
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [images, setImages] = useState<ImageInfo[]>([])
  const [currentIndex, setCurrentIndex] = useState(0)
  const [altText, setAltText] = useState('')
  const [statusMessage, setStatusMessage] = useState<{ text: string; isError: boolean } | null>(null)
  const [loading, setLoading] = useState(false)

  const showStatus = (text: string, isError = false) => {
    setStatusMessage({ text, isError })
    setTimeout(() => setStatusMessage(null), 3000)
  }

  const openModal = async () => {
    setLoading(true)
    try {
      const response = await fetch(`/api/${pdfId}/images/`)
      if (!response.ok) {
        throw new Error('Failed to fetch images')
      }
      const data = await response.json()
      setImages(data.images)
      
      if (data.images.length === 0) {
        showStatus('No images found in PDF', true)
        return
      }
      
      setCurrentIndex(0)
      setAltText('')
      setIsModalOpen(true)
    } catch (error) {
      showStatus(`Error loading images: ${error instanceof Error ? error.message : 'Unknown error'}`, true)
    } finally {
      setLoading(false)
    }
  }

  const closeModal = () => {
    setIsModalOpen(false)
    setAltText('')
    setStatusMessage(null)
  }

  const nextImage = () => {
    if (currentIndex < images.length - 1) {
      setCurrentIndex(currentIndex + 1)
      setAltText('')
      setStatusMessage(null)
    }
  }

  const prevImage = () => {
    if (currentIndex > 0) {
      setCurrentIndex(currentIndex - 1)
      setAltText('')
      setStatusMessage(null)
    }
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    
    const trimmedAltText = altText.trim()
    if (!trimmedAltText) {
      showStatus('Please enter alt text', true)
      return
    }
    
    const currentImage = images[currentIndex]
    
    try {
      const response = await fetch(`/api/${pdfId}/images/${currentImage.id}/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ alt_text: trimmedAltText })
      })
      
      if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.error || 'Failed to save alt text')
      }
      
      showStatus('Alt text saved successfully!')
      
      if (currentIndex < images.length - 1) {
        setTimeout(() => {
          nextImage()
        }, 500)
      }
    } catch (error) {
      showStatus(`Error saving alt text: ${error instanceof Error ? error.message : 'Unknown error'}`, true)
    }
  }

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (!isModalOpen) return
    
    if (e.key === 'ArrowLeft') {
      e.preventDefault()
      prevImage()
    } else if (e.key === 'ArrowRight') {
      e.preventDefault()
      nextImage()
    } else if (e.key === 'Escape') {
      closeModal()
    }
  }

  return (
    <>
      <Tool title="Tag Images">
        <Button 
          onClick={openModal} 
          disabled={loading}
          className="w-full"
        >
          {loading ? 'Loading...' : 'Tag Images'}
        </Button>
      </Tool>

      {isModalOpen && (
        <div 
          className="modal-overlay"
          onClick={(e) => e.target === e.currentTarget && closeModal()}
          onKeyDown={handleKeyDown}
          role="dialog"
          aria-modal="true"
        >
          <div className="modal-content">
            <button
              type="button"
              className="modal-close"
              onClick={closeModal}
              aria-label="Close"
            >
              <X size={20} />
            </button>
            
            <div className="carousel-container">
              <button
                type="button"
                className="nav-button nav-prev"
                onClick={prevImage}
                disabled={currentIndex === 0}
                aria-label="Previous image"
              >
                <ChevronLeft size={24} />
              </button>
              
              <div className="image-display">
                <div className="image-counter">
                  Image {currentIndex + 1} of {images.length}
                </div>
                <img
                  src={`/api/${pdfId}/images/${images[currentIndex].id}/`}
                  alt={`PDF content ${currentIndex + 1} of ${images.length}`}
                  className="carousel-image"
                />
              </div>
              
              <button
                type="button"
                className="nav-button nav-next"
                onClick={nextImage}
                disabled={currentIndex === images.length - 1}
                aria-label="Next image"
              >
                <ChevronRight size={24} />
              </button>
            </div>
            
            <div className="form-container">
              <form onSubmit={handleSubmit} className="alt-text-form">
                <Input
                  type="text"
                  value={altText}
                  onChange={(e) => setAltText(e.target.value)}
                  placeholder="Enter alt text for this image..."
                  className="flex-1"
                />
                <Button type="submit">
                  Save Alt Text
                </Button>
              </form>
              
              {statusMessage && (
                <div className={`status-message ${statusMessage.isError ? 'status-error' : 'status-success'}`}>
                  {statusMessage.text}
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      <style>{`
        .modal-overlay {
          position: fixed;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
          background: rgba(0, 0, 0, 0.8);
          z-index: 1000;
          display: flex;
          justify-content: center;
          align-items: center;
        }

        .modal-content {
          position: relative;
          width: 90%;
          height: 90%;
          background: white;
          border-radius: 0.5rem;
          display: flex;
          flex-direction: column;
          overflow: hidden;
        }

        .modal-close {
          position: absolute;
          top: 1rem;
          right: 1rem;
          width: 2rem;
          height: 2rem;
          background: #ef4444;
          color: white;
          border: none;
          border-radius: 0.25rem;
          cursor: pointer;
          z-index: 10;
          display: flex;
          align-items: center;
          justify-content: center;
          transition: background 0.2s;
        }

        .modal-close:hover {
          background: #dc2626;
        }

        .carousel-container {
          flex: 1;
          display: flex;
          align-items: center;
          justify-content: center;
          position: relative;
          padding: 3rem 4rem 1rem;
          background: #f3f4f6;
        }

        .nav-button {
          position: absolute;
          width: 3rem;
          height: 3rem;
          background: white;
          border: 2px solid #d1d5db;
          border-radius: 50%;
          cursor: pointer;
          display: flex;
          align-items: center;
          justify-content: center;
          transition: all 0.2s;
        }

        .nav-button:hover:not(:disabled) {
          background: #f3f4f6;
          border-color: #9ca3af;
        }

        .nav-button:disabled {
          opacity: 0.5;
          cursor: not-allowed;
        }

        .nav-prev {
          left: 1rem;
        }

        .nav-next {
          right: 1rem;
        }

        .image-display {
          max-width: 100%;
          max-height: 100%;
          display: flex;
          flex-direction: column;
          align-items: center;
          gap: 1rem;
        }

        .image-counter {
          font-size: 0.875rem;
          color: #6b7280;
          font-weight: 500;
        }

        .carousel-image {
          max-width: 100%;
          max-height: calc(90vh - 200px);
          object-fit: contain;
          border-radius: 0.5rem;
          box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .form-container {
          padding: 1.5rem;
          border-top: 1px solid #e5e7eb;
          background: white;
        }

        .alt-text-form {
          display: flex;
          gap: 0.75rem;
        }

        .status-message {
          margin-top: 0.75rem;
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
      `}</style>
    </>
  )
}
