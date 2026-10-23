import 'package:flutter/material.dart';

void main() {
  runApp(const UiUxManualDemo());
}

// Ejemplo ficticio: no consulta APIs ni documentos institucionales reales.
class UiUxManualDemo extends StatelessWidget {
  const UiUxManualDemo({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Manual UI/UX · Ejemplo 01',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: const Color(0xFF0C4CA8)),
        useMaterial3: true,
      ),
      home: const DocumentHomePage(),
    );
  }
}

enum DocumentState { available, pending, error }

class DocumentHomePage extends StatefulWidget {
  const DocumentHomePage({super.key});

  @override
  State<DocumentHomePage> createState() => _DocumentHomePageState();
}

class _DocumentHomePageState extends State<DocumentHomePage> {
  DocumentState _state = DocumentState.available;

  String get _stateText => switch (_state) {
        DocumentState.available => 'Disponible',
        DocumentState.pending => 'Pendiente de emisión',
        DocumentState.error => 'Estado no disponible',
      };

  String get _description => switch (_state) {
        DocumentState.available =>
          'Puedes consultar los detalles de la constancia ficticia.',
        DocumentState.pending =>
          'La institución todavía no ha emitido este documento ficticio.',
        DocumentState.error =>
          'No se pudo consultar el estado. Eso no demuestra que no exista.',
      };

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Mis documentos')),
      body: ListView(
        padding: const EdgeInsets.all(20),
        children: [
          const Text(
            'Demostración educativa con datos ficticios',
            style: TextStyle(fontWeight: FontWeight.w600),
          ),
          const SizedBox(height: 20),
          const Text('Cambiar el estado mostrado:'),
          DropdownButton<DocumentState>(
            value: _state,
            isExpanded: true,
            items: const [
              DropdownMenuItem(
                value: DocumentState.available,
                child: Text('Disponible'),
              ),
              DropdownMenuItem(
                value: DocumentState.pending,
                child: Text('Pendiente de emisión'),
              ),
              DropdownMenuItem(
                value: DocumentState.error,
                child: Text('Error de consulta'),
              ),
            ],
            onChanged: (next) {
              if (next != null) setState(() => _state = next);
            },
          ),
          const SizedBox(height: 12),
          Card(
            child: Padding(
              padding: const EdgeInsets.all(12),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  Text(
                    'Constancia de matrícula',
                    style: Theme.of(context).textTheme.titleLarge,
                  ),
                  const Text('Período lectivo 2026–2027'),
                  const SizedBox(height: 12),
                  Text('Estado: $_stateText'),
                  Text(_description),
                  if (_state == DocumentState.available) ...[
                    const SizedBox(height: 12),
                    FilledButton(
                      onPressed: () {
                        Navigator.of(context).push(
                          MaterialPageRoute<void>(
                            builder: (_) => const DocumentDetailPage(),
                          ),
                        );
                      },
                      child: const Text('Ver información de la constancia'),
                    ),
                  ],
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class DocumentDetailPage extends StatelessWidget {
  const DocumentDetailPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Constancia de matrícula')),
      body: const SafeArea(
        child: Padding(
          padding: EdgeInsets.all(20),
          child: Text(
            'Período lectivo 2026–2027. Esta es una demostración '
            'educativa. No se ha generado, solicitado ni descargado '
            'ningún documento real.',
          ),
        ),
      ),
    );
  }
}
