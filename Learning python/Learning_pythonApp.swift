//
//  Learning_pythonApp.swift
//  Learning python
//
//  Created by Vikkas Arun Pareek on 10/03/2025.
//

import SwiftUI

@main
struct Learning_pythonApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: Learning_pythonDocument()) { file in
            ContentView(document: file.$document)
        }
    }
}
