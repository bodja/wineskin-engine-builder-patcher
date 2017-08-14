from installer.builders.cmake import CMake
from .base import Formula


class OpenalSoft(Formula):
    url = 'http://kcat.strangesoft.net/openal-releases/openal-soft-1.18.1.tar.bz2'  # noqa
    builder_classes = (
        CMake,
    )

    @property
    def options(self):
        return [
            f'-DCMAKE_INSTALL_PREFIX={self.prefix}',
            '-DALSOFT_EXAMPLES=OFF',
            '-DALSOFT_BACKEND_PORTAUDIO=OFF',
            '-DALSOFT_BACKEND_PULSEAUDIO=OFF',
            '-DALSOFT_MIDI_FLUIDSYNTH=OFF'
        ]
