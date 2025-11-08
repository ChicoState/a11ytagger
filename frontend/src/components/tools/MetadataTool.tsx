import { useEffect, useState } from 'react'
import { Tool } from './Tool'

interface MetadataResponse {
  pdf_filename: string
  page_count: number
  pdf_version: string
  file_size_bytes: number
  document_title?: string
  document_language?: string
  is_tagged: boolean
  has_structure_tree: boolean
  is_encrypted: boolean
  total_images: number
  actual_image_count?: number
  images_with_alt_text: number
  images_without_alt_text: number
  structure_types_found?: string[]
  errors?: string[]
  warnings?: string[]
}

interface MetadataToolProps {
  pdfId: string
}

export function MetadataTool({ pdfId }: MetadataToolProps) {
  const [metadata, setMetadata] = useState<MetadataResponse | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const fetchMetadata = async () => {
      try {
        const response = await fetch(`/api/${pdfId}/accessibility_metadata/`)
        if (!response.ok) {
          throw new Error('Failed to fetch metadata')
        }
        const data = await response.json()
        setMetadata(data)
        setLoading(false)
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load metadata')
        setLoading(false)
      }
    }

    fetchMetadata()
  }, [pdfId])

  const formatBytes = (bytes: number) => {
    if (bytes === 0) return '0 Bytes'
    const k = 1024
    const sizes = ['Bytes', 'KB', 'MB', 'GB']
    const i = Math.floor(Math.log(bytes) / Math.log(k))
    return Math.round((bytes / Math.pow(k, i)) * 100) / 100 + ' ' + sizes[i]
  }

  return (
    <Tool title="Metadata" defaultOpen={true}>
      {loading && <p className="text-gray-500 italic">Loading metadata...</p>}
      
      {error && <p className="text-red-600">Error loading metadata: {error}</p>}
      
      {metadata && (
        <div className="space-y-6">
          {/* Document Information */}
          <div className="metadata-section">
            <h3 className="text-base font-semibold mb-2 text-gray-800">Document Information</h3>
            <div className="metadata-grid">
              <span className="metadata-label">Filename:</span>
              <span className="metadata-value">{metadata.pdf_filename || 'N/A'}</span>
              
              <span className="metadata-label">Pages:</span>
              <span className="metadata-value">{metadata.page_count || 0}</span>
              
              <span className="metadata-label">PDF Version:</span>
              <span className="metadata-value">{metadata.pdf_version || 'N/A'}</span>
              
              <span className="metadata-label">File Size:</span>
              <span className="metadata-value">{formatBytes(metadata.file_size_bytes)}</span>
              
              {metadata.document_title && (
                <>
                  <span className="metadata-label">Title:</span>
                  <span className="metadata-value">{metadata.document_title}</span>
                </>
              )}
              
              {metadata.document_language && (
                <>
                  <span className="metadata-label">Language:</span>
                  <span className="metadata-value">{metadata.document_language}</span>
                </>
              )}
            </div>
          </div>

          {/* Accessibility Status */}
          <div className="metadata-section">
            <h3 className="text-base font-semibold mb-2 text-gray-800">Accessibility Status</h3>
            <div className="metadata-grid">
              <span className="metadata-label">Tagged PDF:</span>
              <span className="metadata-value">
                <span className={`status-badge ${metadata.is_tagged ? 'status-success' : 'status-error'}`}>
                  {metadata.is_tagged ? 'Yes' : 'No'}
                </span>
              </span>
              
              <span className="metadata-label">Structure Tree:</span>
              <span className="metadata-value">
                <span className={`status-badge ${metadata.has_structure_tree ? 'status-success' : 'status-error'}`}>
                  {metadata.has_structure_tree ? 'Present' : 'Missing'}
                </span>
              </span>
              
              <span className="metadata-label">Encrypted:</span>
              <span className="metadata-value">
                <span className={`status-badge ${metadata.is_encrypted ? 'status-warning' : 'status-success'}`}>
                  {metadata.is_encrypted ? 'Yes' : 'No'}
                </span>
              </span>
            </div>
          </div>

          {/* Images */}
          {(metadata.total_images > 0 || (metadata.actual_image_count && metadata.actual_image_count > 0)) && (
            <div className="metadata-section">
              <h3 className="text-base font-semibold mb-2 text-gray-800">Images</h3>
              <div className="metadata-grid">
                {metadata.actual_image_count !== undefined && (
                  <>
                    <span className="metadata-label">Total Images in PDF:</span>
                    <span className="metadata-value">{metadata.actual_image_count}</span>
                  </>
                )}
                
                {metadata.total_images > 0 ? (
                  <>
                    <span className="metadata-label">Tagged in Structure:</span>
                    <span className="metadata-value">{metadata.total_images}</span>
                    
                    <span className="metadata-label">With Alt Text:</span>
                    <span className="metadata-value">{metadata.images_with_alt_text}</span>
                    
                    <span className="metadata-label">Without Alt Text:</span>
                    <span className="metadata-value">{metadata.images_without_alt_text}</span>
                  </>
                ) : metadata.actual_image_count && metadata.actual_image_count > 0 ? (
                  <>
                    <span className="metadata-label">Tagged in Structure:</span>
                    <span className="metadata-value">0 (none tagged)</span>
                  </>
                ) : null}
              </div>
            </div>
          )}

          {/* Structure Types */}
          {metadata.structure_types_found && metadata.structure_types_found.length > 0 && (
            <div className="metadata-section">
              <h3 className="text-base font-semibold mb-2 text-gray-800">Structure Elements Found</h3>
              <div className="metadata-value">{metadata.structure_types_found.join(', ')}</div>
            </div>
          )}

          {/* Errors */}
          {metadata.errors && metadata.errors.length > 0 && (
            <div className="metadata-section">
              <h3 className="text-base font-semibold mb-2 text-gray-800">Errors</h3>
              <ul className="message-list">
                {metadata.errors.map((error, idx) => (
                  <li key={idx} className="text-red-700">{error}</li>
                ))}
              </ul>
            </div>
          )}

          {/* Warnings */}
          {metadata.warnings && metadata.warnings.length > 0 && (
            <div className="metadata-section">
              <h3 className="text-base font-semibold mb-2 text-gray-800">Warnings</h3>
              <ul className="message-list">
                {metadata.warnings.map((warning, idx) => (
                  <li key={idx} className="text-orange-600">{warning}</li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}

      <style>{`
        .metadata-section {
          margin-bottom: 1.5rem;
        }

        .metadata-grid {
          display: grid;
          grid-template-columns: auto 1fr;
          gap: 0.5rem;
          font-size: 0.875rem;
        }

        .metadata-label {
          font-weight: 500;
          color: #666;
        }

        .metadata-value {
          color: #333;
          word-wrap: break-word;
          overflow-wrap: break-word;
        }

        .status-badge {
          display: inline-block;
          padding: 0.125rem 0.5rem;
          border-radius: 0.25rem;
          font-size: 0.75rem;
          font-weight: 500;
        }

        .status-success {
          background: #e8f5e9;
          color: #2e7d32;
        }

        .status-error {
          background: #ffebee;
          color: #c62828;
        }

        .status-warning {
          background: #fff3e0;
          color: #ef6c00;
        }

        .message-list {
          margin: 0;
          padding-left: 1.25rem;
          font-size: 0.875rem;
        }
      `}</style>
    </Tool>
  )
}
