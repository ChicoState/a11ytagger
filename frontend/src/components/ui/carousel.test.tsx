import { render, screen, fireEvent } from '@testing-library/react';
import { Carousel, CarouselContent, CarouselItem, CarouselNext, CarouselPrevious } from './carousel';

// Mock Embla Carousel
vi.mock('embla-carousel-react', () => ({
    default: vi.fn(() => [
        { scrollPrev: vi.fn(), scrollNext: vi.fn() },
        {
            canScrollPrev: vi.fn(() => false),
            canScrollNext: vi.fn(() => true),
            on: vi.fn(),
            off: vi.fn() // Add this
        }
    ]),
}));

describe('Carousel', () => {
    it('renders children in carousel content', () => {
        render(
            <Carousel>
                <CarouselContent>
                    <CarouselItem>Slide 1</CarouselItem>
                    <CarouselItem>Slide 2</CarouselItem>
                </CarouselContent>
            </Carousel>
        );
        expect(screen.getByText('Slide 1')).toBeInTheDocument();
        expect(screen.getByText('Slide 2')).toBeInTheDocument();
    });

    it('renders navigation buttons', () => {
        render(
            <Carousel>
                <CarouselContent>
                    <CarouselItem>Slide</CarouselItem>
                </CarouselContent>
                <CarouselPrevious />
                <CarouselNext />
            </Carousel>
        );
        expect(screen.getByRole('button', { name: /previous/i })).toBeInTheDocument();
        expect(screen.getByRole('button', { name: /next/i })).toBeInTheDocument();
    });
});
