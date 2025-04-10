# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestCaseCommentVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uri': 'str',
        'creator': 'str',
        'comment': 'str',
        'notifier': 'list[str]',
        'test_case_uri': 'str',
        'create_time': 'datetime',
        'create_time_timestamp': 'int',
        'update_time': 'datetime',
        'update_time_timestamp': 'int',
        'project_uuid': 'str',
        'version_uri': 'str',
        'display_name': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'creator': 'creator',
        'comment': 'comment',
        'notifier': 'notifier',
        'test_case_uri': 'test_case_uri',
        'create_time': 'create_time',
        'create_time_timestamp': 'create_time_timestamp',
        'update_time': 'update_time',
        'update_time_timestamp': 'update_time_timestamp',
        'project_uuid': 'project_uuid',
        'version_uri': 'version_uri',
        'display_name': 'display_name'
    }

    def __init__(self, uri=None, creator=None, comment=None, notifier=None, test_case_uri=None, create_time=None, create_time_timestamp=None, update_time=None, update_time_timestamp=None, project_uuid=None, version_uri=None, display_name=None):
        r"""TestCaseCommentVo

        The model defined in huaweicloud sdk

        :param uri: 
        :type uri: str
        :param creator: 
        :type creator: str
        :param comment: 
        :type comment: str
        :param notifier: 
        :type notifier: list[str]
        :param test_case_uri: 
        :type test_case_uri: str
        :param create_time: 
        :type create_time: datetime
        :param create_time_timestamp: 创建时间时间戳
        :type create_time_timestamp: int
        :param update_time: 
        :type update_time: datetime
        :param update_time_timestamp: 更新时间时间戳
        :type update_time_timestamp: int
        :param project_uuid: 
        :type project_uuid: str
        :param version_uri: 
        :type version_uri: str
        :param display_name: 
        :type display_name: str
        """
        
        

        self._uri = None
        self._creator = None
        self._comment = None
        self._notifier = None
        self._test_case_uri = None
        self._create_time = None
        self._create_time_timestamp = None
        self._update_time = None
        self._update_time_timestamp = None
        self._project_uuid = None
        self._version_uri = None
        self._display_name = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if creator is not None:
            self.creator = creator
        if comment is not None:
            self.comment = comment
        if notifier is not None:
            self.notifier = notifier
        if test_case_uri is not None:
            self.test_case_uri = test_case_uri
        if create_time is not None:
            self.create_time = create_time
        if create_time_timestamp is not None:
            self.create_time_timestamp = create_time_timestamp
        if update_time is not None:
            self.update_time = update_time
        if update_time_timestamp is not None:
            self.update_time_timestamp = update_time_timestamp
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if version_uri is not None:
            self.version_uri = version_uri
        if display_name is not None:
            self.display_name = display_name

    @property
    def uri(self):
        r"""Gets the uri of this TestCaseCommentVo.

        :return: The uri of this TestCaseCommentVo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this TestCaseCommentVo.

        :param uri: The uri of this TestCaseCommentVo.
        :type uri: str
        """
        self._uri = uri

    @property
    def creator(self):
        r"""Gets the creator of this TestCaseCommentVo.

        :return: The creator of this TestCaseCommentVo.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this TestCaseCommentVo.

        :param creator: The creator of this TestCaseCommentVo.
        :type creator: str
        """
        self._creator = creator

    @property
    def comment(self):
        r"""Gets the comment of this TestCaseCommentVo.

        :return: The comment of this TestCaseCommentVo.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this TestCaseCommentVo.

        :param comment: The comment of this TestCaseCommentVo.
        :type comment: str
        """
        self._comment = comment

    @property
    def notifier(self):
        r"""Gets the notifier of this TestCaseCommentVo.

        :return: The notifier of this TestCaseCommentVo.
        :rtype: list[str]
        """
        return self._notifier

    @notifier.setter
    def notifier(self, notifier):
        r"""Sets the notifier of this TestCaseCommentVo.

        :param notifier: The notifier of this TestCaseCommentVo.
        :type notifier: list[str]
        """
        self._notifier = notifier

    @property
    def test_case_uri(self):
        r"""Gets the test_case_uri of this TestCaseCommentVo.

        :return: The test_case_uri of this TestCaseCommentVo.
        :rtype: str
        """
        return self._test_case_uri

    @test_case_uri.setter
    def test_case_uri(self, test_case_uri):
        r"""Sets the test_case_uri of this TestCaseCommentVo.

        :param test_case_uri: The test_case_uri of this TestCaseCommentVo.
        :type test_case_uri: str
        """
        self._test_case_uri = test_case_uri

    @property
    def create_time(self):
        r"""Gets the create_time of this TestCaseCommentVo.

        :return: The create_time of this TestCaseCommentVo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TestCaseCommentVo.

        :param create_time: The create_time of this TestCaseCommentVo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def create_time_timestamp(self):
        r"""Gets the create_time_timestamp of this TestCaseCommentVo.

        创建时间时间戳

        :return: The create_time_timestamp of this TestCaseCommentVo.
        :rtype: int
        """
        return self._create_time_timestamp

    @create_time_timestamp.setter
    def create_time_timestamp(self, create_time_timestamp):
        r"""Sets the create_time_timestamp of this TestCaseCommentVo.

        创建时间时间戳

        :param create_time_timestamp: The create_time_timestamp of this TestCaseCommentVo.
        :type create_time_timestamp: int
        """
        self._create_time_timestamp = create_time_timestamp

    @property
    def update_time(self):
        r"""Gets the update_time of this TestCaseCommentVo.

        :return: The update_time of this TestCaseCommentVo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this TestCaseCommentVo.

        :param update_time: The update_time of this TestCaseCommentVo.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def update_time_timestamp(self):
        r"""Gets the update_time_timestamp of this TestCaseCommentVo.

        更新时间时间戳

        :return: The update_time_timestamp of this TestCaseCommentVo.
        :rtype: int
        """
        return self._update_time_timestamp

    @update_time_timestamp.setter
    def update_time_timestamp(self, update_time_timestamp):
        r"""Sets the update_time_timestamp of this TestCaseCommentVo.

        更新时间时间戳

        :param update_time_timestamp: The update_time_timestamp of this TestCaseCommentVo.
        :type update_time_timestamp: int
        """
        self._update_time_timestamp = update_time_timestamp

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this TestCaseCommentVo.

        :return: The project_uuid of this TestCaseCommentVo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this TestCaseCommentVo.

        :param project_uuid: The project_uuid of this TestCaseCommentVo.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def version_uri(self):
        r"""Gets the version_uri of this TestCaseCommentVo.

        :return: The version_uri of this TestCaseCommentVo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this TestCaseCommentVo.

        :param version_uri: The version_uri of this TestCaseCommentVo.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def display_name(self):
        r"""Gets the display_name of this TestCaseCommentVo.

        :return: The display_name of this TestCaseCommentVo.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this TestCaseCommentVo.

        :param display_name: The display_name of this TestCaseCommentVo.
        :type display_name: str
        """
        self._display_name = display_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TestCaseCommentVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
