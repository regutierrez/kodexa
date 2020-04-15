# generated by datamodel-codegen:
#   filename:  kodexa-swagger.json
#   timestamp: 2020-04-15T17:50:25+00:00

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class Model(BaseModel):
    __root__: 'Any'


class BotEventTrigger(BaseModel):
    cellId: Optional[str] = None
    event: Optional[str] = None
    type: Optional[str] = None


class CellProcessor(BaseModel):
    condition: Optional[str] = None
    configuration: Optional[Dict[str, Any]] = None
    targetCellId: Optional[str] = None
    type: Optional[str] = None


class SessionState(Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'


class SessionState1(Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'


class Type(Enum):
    START_EXECUTION = 'START_EXECUTION'
    STEP_UPDATE = 'STEP_UPDATE'
    BOT_NOTIFICATION = 'BOT_NOTIFICATION'


class Status(Enum):
    PENDING = 'PENDING'
    RUNNING = 'RUNNING'
    SUCCEEDED = 'SUCCEEDED'
    FAILED = 'FAILED'
    REQUESTED = 'REQUESTED'


class Status1(Enum):
    PENDING = 'PENDING'
    RUNNING = 'RUNNING'
    SUCCEEDED = 'SUCCEEDED'
    FAILED = 'FAILED'
    REQUESTED = 'REQUESTED'


class SessionState2(Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'


class SessionState3(Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'


class CloudStore(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None


class ContentType(Enum):
    DOCUMENT = 'DOCUMENT'
    NATIVE = 'NATIVE'


class ContentObject(BaseModel):
    contentType: Optional['ContentType'] = None
    id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    name: Optional[str] = None
    tags: Optional[List[str]] = None


class ContentServiceReference(BaseModel):
    attachSource: Optional[bool] = None
    contentServiceId: Optional[str] = None
    contentServiceVersionId: Optional[str] = None
    ref: Optional[str] = None


class DeploymentMetadata(BaseModel):
    accessToken: Optional[str] = None
    botId: Optional[str] = None
    type: str


class EmailDeployment(DeploymentMetadata):
    accessToken: Optional[str] = None
    address: Optional[str] = None
    botId: Optional[str] = None
    type: str


class EmailLookup(BaseModel):
    email: Optional[str] = None
    id: Optional[str] = None


class ExceptionDetails(BaseModel):
    errorMessage: Optional[str] = None
    errorType: Optional[str] = None
    executedVersion: Optional[str] = None
    help: Optional[str] = None
    message: Optional[str] = None
    stackTrace: Optional[List[Dict[str, Any]]] = None
    statusCode: Optional[int] = None


class ExceptionReport(BaseModel):
    description: Optional[str] = None
    exceptionUuid: Optional[str] = None
    message: Optional[str] = None
    platform: Optional[str] = None


class Feedback(BaseModel):
    createdBy: Optional[str] = None
    createdOn: Optional[str] = None
    feedback: Optional[str] = None
    id: Optional[str] = None
    updatedBy: Optional[str] = None
    updatedOn: Optional[str] = None
    uuid: Optional[str] = None


class File(BaseModel):
    absolute: Optional[bool] = None
    absoluteFile: Optional['File'] = None
    absolutePath: Optional[str] = None
    canonicalFile: Optional['File'] = None
    canonicalPath: Optional[str] = None
    directory: Optional[bool] = None
    file: Optional[bool] = None
    freeSpace: Optional[int] = None
    hidden: Optional[bool] = None
    name: Optional[str] = None
    parent: Optional[str] = None
    parentFile: Optional['File'] = None
    path: Optional[str] = None
    totalSpace: Optional[int] = None
    usableSpace: Optional[int] = None


class Type1(Enum):
    PIPELINE = 'PIPELINE'
    ACTION = 'ACTION'
    DECISION = 'DECISION'


class GraphCell(BaseModel):
    id: Optional[str] = None
    options: Optional[Dict[str, Any]] = None
    post: Optional[List['CellProcessor']] = None
    pre: Optional[List['CellProcessor']] = None
    ref: Optional[str] = None
    type: Optional['Type1'] = None


class InputStream(BaseModel):
    pass


class LoginRequest(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None


class Role(Enum):
    OWNER = 'OWNER'
    READ = 'READ'
    WRITE = 'WRITE'


class Organization(BaseModel):
    createdBy: Optional[str] = None
    createdOn: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    publicAccess: Optional[bool] = None
    slug: Optional[str] = None
    updatedBy: Optional[str] = None
    updatedOn: Optional[str] = None
    uuid: Optional[str] = None


class OrganizationDashboard(BaseModel):
    pipelineCount: Optional[int] = None
    requestCount: Optional[int] = None
    serviceCount: Optional[int] = None
    userCount: Optional[int] = None


class PasswordChange(BaseModel):
    newPassword: Optional[str] = None
    oldPassword: Optional[str] = None


class PipelineStepMetadata(BaseModel):
    name: Optional[str] = None
    options: Optional[Dict[str, Any]] = None
    organizationSlug: Optional[str] = None
    slug: Optional[str] = None


class PlatformOverview(BaseModel):
    buildTime: Optional[str] = None
    commitId: Optional[str] = None
    dsn: Optional[str] = None
    environment: Optional[str] = None
    hostName: Optional[str] = None
    name: Optional[str] = None
    release: Optional[str] = None
    version: Optional[str] = None


class RegisterUser(BaseModel):
    email: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None


class SlackDeployment(DeploymentMetadata):
    accessToken: Optional[str] = None
    botId: Optional[str] = None
    channelId: Optional[str] = None
    type: str


class Sort(BaseModel):
    empty: Optional[bool] = None
    sorted: Optional[bool] = None
    unsorted: Optional[bool] = None


class SubscriptionResponse(BaseModel):
    alert: Optional[str] = None
    message: Optional[str] = None


class Timestamp(BaseModel):
    date: Optional[int] = None
    day: Optional[int] = None
    hours: Optional[int] = None
    minutes: Optional[int] = None
    month: Optional[int] = None
    nanos: Optional[int] = None
    seconds: Optional[int] = None
    time: Optional[int] = None
    timezoneOffset: Optional[int] = None
    year: Optional[int] = None


class URI(BaseModel):
    absolute: Optional[bool] = None
    authority: Optional[str] = None
    fragment: Optional[str] = None
    host: Optional[str] = None
    opaque: Optional[bool] = None
    path: Optional[str] = None
    port: Optional[int] = None
    query: Optional[str] = None
    rawAuthority: Optional[str] = None
    rawFragment: Optional[str] = None
    rawPath: Optional[str] = None
    rawQuery: Optional[str] = None
    rawSchemeSpecificPart: Optional[str] = None
    rawUserInfo: Optional[str] = None
    scheme: Optional[str] = None
    schemeSpecificPart: Optional[str] = None
    userInfo: Optional[str] = None


class URL(BaseModel):
    authority: Optional[str] = None
    content: Optional[Dict[str, Any]] = None
    defaultPort: Optional[int] = None
    file: Optional[str] = None
    host: Optional[str] = None
    path: Optional[str] = None
    port: Optional[int] = None
    protocol: Optional[str] = None
    query: Optional[str] = None
    ref: Optional[str] = None
    userInfo: Optional[str] = None


class UserActivation(BaseModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    password: Optional[str] = None


class View(BaseModel):
    contentType: Optional[str] = None


class AccessToken(BaseModel):
    createdBy: Optional[str] = None
    createdOn: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    organization: Optional['Organization'] = None
    token: Optional[str] = None
    updatedBy: Optional[str] = None
    updatedOn: Optional[str] = None
    uuid: Optional[str] = None


class BotMetadata(BaseModel):
    createSession: Optional[bool] = None
    graphCells: Optional[List['GraphCell']] = None
    triggers: Optional[List['BotEventTrigger']] = None


class ByteArrayResource(BaseModel):
    byteArray: Optional[str] = None
    description: Optional[str] = None
    file: Optional['File'] = None
    filename: Optional[str] = None
    inputStream: Optional['InputStream'] = None
    open: Optional[bool] = None
    readable: Optional[bool] = None
    uri: Optional['URI'] = None
    url: Optional['URL'] = None


class CloudExecutionStep(BaseModel):
    contentObjects: Optional[List[Dict[str, Any]]] = None
    contentServiceReference: Optional['ContentServiceReference'] = None
    context: Optional[Dict[str, Any]] = None
    end: Optional[datetime] = None
    exceptionDetails: Optional['ExceptionDetails'] = None
    id: Optional[str] = None
    options: Optional[Dict[str, Any]] = None
    processingTime: Optional[int] = None
    start: Optional[datetime] = None
    status: Optional['Status1'] = None
    stores: Optional[List['CloudStore']] = None


class CloudPipeline(BaseModel):
    exceptions: Optional[List['ExceptionDetails']] = None
    id: Optional[str] = None
    ref: Optional[str] = None
    steps: Optional[List['CloudExecutionStep']] = None
    valid: Optional[bool] = None


class CloudSession(BaseModel):
    contentObjects: Optional[List[Dict[str, Any]]] = None
    id: str
    lastAccessed: Optional[int] = None
    pipelineTemplates: Optional[List['CloudPipeline']] = None
    sessionState: 'SessionState3'
    type: str


class ContentService(BaseModel):
    createdBy: Optional[str] = None
    createdOn: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    name: Optional[str] = None
    organization: Optional['Organization'] = None
    publicAccess: Optional[bool] = None
    ref: Optional[str] = None
    slug: Optional[str] = None
    updatedBy: Optional[str] = None
    updatedOn: Optional[str] = None
    uuid: Optional[str] = None


class ContentServiceVersion(BaseModel):
    contentService: Optional['ContentService'] = None
    createdBy: Optional[str] = None
    createdOn: Optional[str] = None
    id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    position: Optional[int] = None
    publicAccess: Optional[bool] = None
    updatedBy: Optional[str] = None
    updatedOn: Optional[str] = None
    uuid: Optional[str] = None
    version: Optional[str] = None


class Deployment(BaseModel):
    createdBy: Optional[str] = None
    createdOn: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    metadata: Optional['DeploymentMetadata'] = None
    name: Optional[str] = None
    organization: Optional['Organization'] = None
    updatedBy: Optional[str] = None
    updatedOn: Optional[str] = None
    uuid: Optional[str] = None


class Pageable(BaseModel):
    offset: Optional[int] = None
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None
    paged: Optional[bool] = None
    sort: Optional['Sort'] = None
    unpaged: Optional[bool] = None


class PipelineMetadata(BaseModel):
    steps: Optional[List['PipelineStepMetadata']] = None


class PlatformUser(BaseModel):
    activated: Optional[bool] = None
    createdBy: Optional[str] = None
    createdOn: Optional[str] = None
    email: Optional[str] = None
    firstName: Optional[str] = None
    id: Optional[str] = None
    lastName: Optional[str] = None
    passwordResetDate: Optional['Timestamp'] = None
    platformAdmin: Optional[bool] = None
    updatedBy: Optional[str] = None
    updatedOn: Optional[str] = None
    uuid: Optional[str] = None


class Bot(BaseModel):
    createdBy: Optional[str] = None
    createdOn: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    metadata: Optional['BotMetadata'] = None
    name: Optional[str] = None
    organization: Optional['Organization'] = None
    updatedBy: Optional[str] = None
    updatedOn: Optional[str] = None
    uuid: Optional[str] = None


class CloudBotSession(CloudSession):
    bot: Optional['Bot'] = None
    botState: Optional[Dict[str, Any]] = None
    contentObjects: Optional[List[Dict[str, Any]]] = None
    id: str
    lastAccessed: Optional[int] = None
    pipelineTemplates: Optional[List['CloudPipeline']] = None
    sessionState: 'SessionState'
    type: str


class CloudContentServiceSession(CloudSession):
    contentObjects: Optional[List[Dict[str, Any]]] = None
    contentService: Optional['ContentService'] = None
    id: str
    lastAccessed: Optional[int] = None
    pipelineTemplates: Optional[List['CloudPipeline']] = None
    sessionState: 'SessionState1'
    type: str


class CloudEvent(BaseModel):
    contentObjects: Optional[List['ContentObject']] = None
    executionId: Optional[str] = None
    id: str
    payload: Optional[Dict[str, Any]] = None
    sessionId: str
    source: Optional[Dict[str, Any]] = None
    step: Optional['CloudExecutionStep'] = None
    subType: Optional[str] = None
    type: 'Type'


class CloudExecution(BaseModel):
    contentObjects: Optional[List['ContentObject']] = None
    context: Optional[Dict[str, Any]] = None
    customOptions: Optional[Dict[str, Any]] = None
    end: Optional[datetime] = None
    exceptionDetails: Optional['ExceptionDetails'] = None
    id: Optional[str] = None
    numberOfSteps: Optional[int] = None
    pipelineTemplateId: Optional[str] = None
    processingTime: Optional[int] = None
    sessionId: Optional[str] = None
    start: Optional[datetime] = None
    status: Optional['Status'] = None
    steps: Optional[List['CloudExecutionStep']] = None
    stepsCompleted: Optional[int] = None
    stores: Optional[List['CloudStore']] = None


class Membership(BaseModel):
    createdBy: Optional[str] = None
    createdOn: Optional[str] = None
    id: Optional[str] = None
    organization: Optional['Organization'] = None
    role: Optional['Role'] = None
    updatedBy: Optional[str] = None
    updatedOn: Optional[str] = None
    user: Optional['PlatformUser'] = None
    uuid: Optional[str] = None


class PageOfAccessToken(BaseModel):
    content: Optional[List['AccessToken']] = None
    empty: Optional[bool] = None
    first: Optional[bool] = None
    last: Optional[bool] = None
    number: Optional[int] = None
    numberOfElements: Optional[int] = None
    pageable: Optional['Pageable'] = None
    size: Optional[int] = None
    sort: Optional['Sort'] = None
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None


class PageOfBot(BaseModel):
    content: Optional[List['Bot']] = None
    empty: Optional[bool] = None
    first: Optional[bool] = None
    last: Optional[bool] = None
    number: Optional[int] = None
    numberOfElements: Optional[int] = None
    pageable: Optional['Pageable'] = None
    size: Optional[int] = None
    sort: Optional['Sort'] = None
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None


class PageOfCloudEvent(BaseModel):
    content: Optional[List['CloudEvent']] = None
    empty: Optional[bool] = None
    first: Optional[bool] = None
    last: Optional[bool] = None
    number: Optional[int] = None
    numberOfElements: Optional[int] = None
    pageable: Optional['Pageable'] = None
    size: Optional[int] = None
    sort: Optional['Sort'] = None
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None


class PageOfContentService(BaseModel):
    content: Optional[List['ContentService']] = None
    empty: Optional[bool] = None
    first: Optional[bool] = None
    last: Optional[bool] = None
    number: Optional[int] = None
    numberOfElements: Optional[int] = None
    pageable: Optional['Pageable'] = None
    size: Optional[int] = None
    sort: Optional['Sort'] = None
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None


class PageOfContentServiceVersion(BaseModel):
    content: Optional[List['ContentServiceVersion']] = None
    empty: Optional[bool] = None
    first: Optional[bool] = None
    last: Optional[bool] = None
    number: Optional[int] = None
    numberOfElements: Optional[int] = None
    pageable: Optional['Pageable'] = None
    size: Optional[int] = None
    sort: Optional['Sort'] = None
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None


class PageOfDeployment(BaseModel):
    content: Optional[List['Deployment']] = None
    empty: Optional[bool] = None
    first: Optional[bool] = None
    last: Optional[bool] = None
    number: Optional[int] = None
    numberOfElements: Optional[int] = None
    pageable: Optional['Pageable'] = None
    size: Optional[int] = None
    sort: Optional['Sort'] = None
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None


class PageOfMembership(BaseModel):
    content: Optional[List['Membership']] = None
    empty: Optional[bool] = None
    first: Optional[bool] = None
    last: Optional[bool] = None
    number: Optional[int] = None
    numberOfElements: Optional[int] = None
    pageable: Optional['Pageable'] = None
    size: Optional[int] = None
    sort: Optional['Sort'] = None
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None


class PageOfOrganization(BaseModel):
    content: Optional[List['Organization']] = None
    empty: Optional[bool] = None
    first: Optional[bool] = None
    last: Optional[bool] = None
    number: Optional[int] = None
    numberOfElements: Optional[int] = None
    pageable: Optional['Pageable'] = None
    size: Optional[int] = None
    sort: Optional['Sort'] = None
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None


class PageOfPlatformUser(BaseModel):
    content: Optional[List['PlatformUser']] = None
    empty: Optional[bool] = None
    first: Optional[bool] = None
    last: Optional[bool] = None
    number: Optional[int] = None
    numberOfElements: Optional[int] = None
    pageable: Optional['Pageable'] = None
    size: Optional[int] = None
    sort: Optional['Sort'] = None
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None


class Pipeline(BaseModel):
    createdBy: Optional[str] = None
    createdOn: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    metadata: Optional['PipelineMetadata'] = None
    name: Optional[str] = None
    organization: Optional['Organization'] = None
    publicAccess: Optional[bool] = None
    ref: Optional[str] = None
    slug: Optional[str] = None
    updatedBy: Optional[str] = None
    updatedOn: Optional[str] = None
    uuid: Optional[str] = None


class ServiceRequest(BaseModel):
    contentService: Optional['ContentService'] = None
    contentServiceVersion: Optional['ContentServiceVersion'] = None
    createdBy: Optional[str] = None
    createdOn: Optional[str] = None
    elapsedTime: Optional[int] = None
    id: Optional[str] = None
    internalRequestId: Optional[str] = None
    organization: Optional['Organization'] = None
    pipeline: Optional['Pipeline'] = None
    updatedBy: Optional[str] = None
    updatedOn: Optional[str] = None
    uuid: Optional[str] = None


class CloudPipelineSession(CloudSession):
    contentObjects: Optional[List[Dict[str, Any]]] = None
    id: str
    lastAccessed: Optional[int] = None
    pipeline: Optional['Pipeline'] = None
    pipelineTemplates: Optional[List['CloudPipeline']] = None
    sessionState: 'SessionState2'
    type: str


class PageOfPipeline(BaseModel):
    content: Optional[List['Pipeline']] = None
    empty: Optional[bool] = None
    first: Optional[bool] = None
    last: Optional[bool] = None
    number: Optional[int] = None
    numberOfElements: Optional[int] = None
    pageable: Optional['Pageable'] = None
    size: Optional[int] = None
    sort: Optional['Sort'] = None
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None


class PageOfServiceRequest(BaseModel):
    content: Optional[List['ServiceRequest']] = None
    empty: Optional[bool] = None
    first: Optional[bool] = None
    last: Optional[bool] = None
    number: Optional[int] = None
    numberOfElements: Optional[int] = None
    pageable: Optional['Pageable'] = None
    size: Optional[int] = None
    sort: Optional['Sort'] = None
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None


File.update_forward_refs()
