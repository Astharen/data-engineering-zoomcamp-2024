# To initialize: terraform init -> .terraform.lock.hcl and .terraform creation
# terraform plan: review the changes
# terraform apply: to deploy -> .terraform.tfstate
# terraform destroy: to destroy the deployed resources

terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  # Credentials only needs to be set if you do not have the GOOGLE_APPLICATION_CREDENTIALS set
  credentials = "./keys/my-creds.json"
  project     = "terraform-412019"
  region      = "us-central1"
}



resource "google_storage_bucket" "data-lake-bucket" {
  name     = "terraform-412019-terra-bucket"
  location = "US"

  # Optional, but recommended settings:
  storage_class               = "STANDARD"
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 30 // days
    }
  }

  force_destroy = true
}