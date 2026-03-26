# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetBucketDisPolicyRequestBodyRules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "SetBucketDisPolicyRequestBodyRules"

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'stream': 'str',
        'project': 'str',
        'events': 'list[str]',
        'prefix': 'str',
        'suffix': 'str',
        'agency': 'str'
    }

    attribute_map = {
        'id': 'id',
        'stream': 'stream',
        'project': 'project',
        'events': 'events',
        'prefix': 'prefix',
        'suffix': 'suffix',
        'agency': 'agency'
    }

    def __init__(self, id=None, stream=None, project=None, events=None, prefix=None, suffix=None, agency=None):
        r"""SetBucketDisPolicyRequestBodyRules

        The model defined in huaweicloud sdk

        :param id: Rule ID. The unique identifier of the DIS policy rule configured on the current bucket. Type: String Value range: [1, 256], must satisfy the pattern ^[a-zA-Z0-9_-]{1,256}$.
        :type id: str
        :param stream: DIS service stream name. This stream must be created in the DIS service beforehand. Type: String
        :type stream: str
        :param project: Project ID to which the DIS service stream belongs. Type: String
        :type project: str
        :param events: OBS event list. Valid values: length [0, 1023], any characters allowed; supported event types: ObjectCreated:*, ObjectCreated:Put, ObjectCreated:Post, ObjectCreated:Copy, ObjectCreated:CompleteMultipartUpload, ObjectRemoved:*, ObjectRemoved:Delete, ObjectRemoved:DeleteMarkerCreated.
        :type events: list[str]
        :param prefix: Object name prefix: used to specify keyword-based filtering for object names. Objects are matched based on the defined prefix; a longer prefix provides higher matching precision. The maximum supported length is 1024 characters, and the minimum can be empty. The combined length of the prefix and suffix must not exceed 1024 characters. Type: String Value range: [0, 1024]
        :type prefix: str
        :param suffix: Object name suffix: used to specify keyword-based filtering for object names. Objects are matched based on the defined suffix; a longer suffix provides higher matching precision. The maximum supported length is 1024 characters, and the minimum can be empty. The combined length of the prefix and suffix must not exceed 1024 characters. Type: String Value range: [0, 1024]
        :type suffix: str
        :param agency: IAM agency name. The trusted entity must include the OBS service, and the granted permissions must be **DIS Administrator** or **DIS User** of the DIS service. Type: String
        :type agency: str
        """
        
        

        self._id = None
        self._stream = None
        self._project = None
        self._events = None
        self._prefix = None
        self._suffix = None
        self._agency = None
        self.discriminator = None

        self.id = id
        self.stream = stream
        self.project = project
        self.events = events
        if prefix is not None:
            self.prefix = prefix
        if suffix is not None:
            self.suffix = suffix
        self.agency = agency

    @property
    def id(self):
        r"""Gets the id of this SetBucketDisPolicyRequestBodyRules.

        Rule ID. The unique identifier of the DIS policy rule configured on the current bucket. Type: String Value range: [1, 256], must satisfy the pattern ^[a-zA-Z0-9_-]{1,256}$.

        :return: The id of this SetBucketDisPolicyRequestBodyRules.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SetBucketDisPolicyRequestBodyRules.

        Rule ID. The unique identifier of the DIS policy rule configured on the current bucket. Type: String Value range: [1, 256], must satisfy the pattern ^[a-zA-Z0-9_-]{1,256}$.

        :param id: The id of this SetBucketDisPolicyRequestBodyRules.
        :type id: str
        """
        self._id = id

    @property
    def stream(self):
        r"""Gets the stream of this SetBucketDisPolicyRequestBodyRules.

        DIS service stream name. This stream must be created in the DIS service beforehand. Type: String

        :return: The stream of this SetBucketDisPolicyRequestBodyRules.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        r"""Sets the stream of this SetBucketDisPolicyRequestBodyRules.

        DIS service stream name. This stream must be created in the DIS service beforehand. Type: String

        :param stream: The stream of this SetBucketDisPolicyRequestBodyRules.
        :type stream: str
        """
        self._stream = stream

    @property
    def project(self):
        r"""Gets the project of this SetBucketDisPolicyRequestBodyRules.

        Project ID to which the DIS service stream belongs. Type: String

        :return: The project of this SetBucketDisPolicyRequestBodyRules.
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        r"""Sets the project of this SetBucketDisPolicyRequestBodyRules.

        Project ID to which the DIS service stream belongs. Type: String

        :param project: The project of this SetBucketDisPolicyRequestBodyRules.
        :type project: str
        """
        self._project = project

    @property
    def events(self):
        r"""Gets the events of this SetBucketDisPolicyRequestBodyRules.

        OBS event list. Valid values: length [0, 1023], any characters allowed; supported event types: ObjectCreated:*, ObjectCreated:Put, ObjectCreated:Post, ObjectCreated:Copy, ObjectCreated:CompleteMultipartUpload, ObjectRemoved:*, ObjectRemoved:Delete, ObjectRemoved:DeleteMarkerCreated.

        :return: The events of this SetBucketDisPolicyRequestBodyRules.
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this SetBucketDisPolicyRequestBodyRules.

        OBS event list. Valid values: length [0, 1023], any characters allowed; supported event types: ObjectCreated:*, ObjectCreated:Put, ObjectCreated:Post, ObjectCreated:Copy, ObjectCreated:CompleteMultipartUpload, ObjectRemoved:*, ObjectRemoved:Delete, ObjectRemoved:DeleteMarkerCreated.

        :param events: The events of this SetBucketDisPolicyRequestBodyRules.
        :type events: list[str]
        """
        self._events = events

    @property
    def prefix(self):
        r"""Gets the prefix of this SetBucketDisPolicyRequestBodyRules.

        Object name prefix: used to specify keyword-based filtering for object names. Objects are matched based on the defined prefix; a longer prefix provides higher matching precision. The maximum supported length is 1024 characters, and the minimum can be empty. The combined length of the prefix and suffix must not exceed 1024 characters. Type: String Value range: [0, 1024]

        :return: The prefix of this SetBucketDisPolicyRequestBodyRules.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this SetBucketDisPolicyRequestBodyRules.

        Object name prefix: used to specify keyword-based filtering for object names. Objects are matched based on the defined prefix; a longer prefix provides higher matching precision. The maximum supported length is 1024 characters, and the minimum can be empty. The combined length of the prefix and suffix must not exceed 1024 characters. Type: String Value range: [0, 1024]

        :param prefix: The prefix of this SetBucketDisPolicyRequestBodyRules.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def suffix(self):
        r"""Gets the suffix of this SetBucketDisPolicyRequestBodyRules.

        Object name suffix: used to specify keyword-based filtering for object names. Objects are matched based on the defined suffix; a longer suffix provides higher matching precision. The maximum supported length is 1024 characters, and the minimum can be empty. The combined length of the prefix and suffix must not exceed 1024 characters. Type: String Value range: [0, 1024]

        :return: The suffix of this SetBucketDisPolicyRequestBodyRules.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        r"""Sets the suffix of this SetBucketDisPolicyRequestBodyRules.

        Object name suffix: used to specify keyword-based filtering for object names. Objects are matched based on the defined suffix; a longer suffix provides higher matching precision. The maximum supported length is 1024 characters, and the minimum can be empty. The combined length of the prefix and suffix must not exceed 1024 characters. Type: String Value range: [0, 1024]

        :param suffix: The suffix of this SetBucketDisPolicyRequestBodyRules.
        :type suffix: str
        """
        self._suffix = suffix

    @property
    def agency(self):
        r"""Gets the agency of this SetBucketDisPolicyRequestBodyRules.

        IAM agency name. The trusted entity must include the OBS service, and the granted permissions must be **DIS Administrator** or **DIS User** of the DIS service. Type: String

        :return: The agency of this SetBucketDisPolicyRequestBodyRules.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        r"""Sets the agency of this SetBucketDisPolicyRequestBodyRules.

        IAM agency name. The trusted entity must include the OBS service, and the granted permissions must be **DIS Administrator** or **DIS User** of the DIS service. Type: String

        :param agency: The agency of this SetBucketDisPolicyRequestBodyRules.
        :type agency: str
        """
        self._agency = agency

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SetBucketDisPolicyRequestBodyRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
