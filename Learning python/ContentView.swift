//
//  ContentView.swift
//  Learning python
//
//  Created by Vikkas Arun Pareek on 10/03/2025.
//

import SwiftUI

struct ContentView: View {
    @Binding var document: Learning_pythonDocument

    var body: some View {
        TextEditor(text: $document.text)
    }
}

#Preview {
    ContentView(document: .constant(Learning_pythonDocument()))
}
