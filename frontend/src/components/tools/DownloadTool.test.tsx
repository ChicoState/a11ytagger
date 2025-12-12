import { render, screen, fireEvent, waitFor, act } from '@testing-library/react';
import { DownloadTool } from './DownloadTool';
import { MemoryRouter } from 'react-router-dom';

// Mock React Router
const mockNavigate = vi.fn();
vi.mock('react-router-dom', async () => {
    const actual = await vi.importActual('react-router-dom');
    return {
        ...actual,
        useNavigate: () => mockNavigate,
    };
});

// Mock fetch
global.fetch = vi.fn();

describe('DownloadTool', () => {
    beforeEach(() => {
        vi.clearAllMocks();
        vi.useFakeTimers();
        (global.fetch as any).mockResolvedValue({ ok: true });
    });

    afterEach(() => {
        vi.useRealTimers();
    });

    it('renders title and download link', () => {
        render(<DownloadTool pdfId="123" />, { wrapper: MemoryRouter });
        expect(screen.getByText('Download & Exit')).toBeInTheDocument();
        expect(screen.getByText('Download PDF')).toBeInTheDocument();
    });

    it('handles exit with confirmation', async () => {
        const mockConfirm = vi.spyOn(window, 'confirm').mockReturnValue(true);

        render(<DownloadTool pdfId="123" />, { wrapper: MemoryRouter });

        await act(async () => {
            fireEvent.click(screen.getByText('Exit & Clean Up'));
        });

        expect(global.fetch).toHaveBeenCalledWith('/api/123/cleanup/', { method: 'POST' });

        vi.advanceTimersByTime(1000);

        expect(mockNavigate).toHaveBeenCalledWith('/');

        mockConfirm.mockRestore();
    });
});