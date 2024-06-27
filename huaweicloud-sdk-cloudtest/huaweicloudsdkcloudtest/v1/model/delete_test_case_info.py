# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTestCaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_uuid': 'str',
        'version_uri': 'str',
        'case_ids': 'list[str]'
    }

    attribute_map = {
        'project_uuid': 'project_uuid',
        'version_uri': 'version_uri',
        'case_ids': 'case_ids'
    }

    def __init__(self, project_uuid=None, version_uri=None, case_ids=None):
        """DeleteTestCaseInfo

        The model defined in huaweicloud sdk

        :param project_uuid: 项目id
        :type project_uuid: str
        :param version_uri: 分支uri
        :type version_uri: str
        :param case_ids: 用例id列表
        :type case_ids: list[str]
        """
        
        

        self._project_uuid = None
        self._version_uri = None
        self._case_ids = None
        self.discriminator = None

        if project_uuid is not None:
            self.project_uuid = project_uuid
        if version_uri is not None:
            self.version_uri = version_uri
        self.case_ids = case_ids

    @property
    def project_uuid(self):
        """Gets the project_uuid of this DeleteTestCaseInfo.

        项目id

        :return: The project_uuid of this DeleteTestCaseInfo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this DeleteTestCaseInfo.

        项目id

        :param project_uuid: The project_uuid of this DeleteTestCaseInfo.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def version_uri(self):
        """Gets the version_uri of this DeleteTestCaseInfo.

        分支uri

        :return: The version_uri of this DeleteTestCaseInfo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        """Sets the version_uri of this DeleteTestCaseInfo.

        分支uri

        :param version_uri: The version_uri of this DeleteTestCaseInfo.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def case_ids(self):
        """Gets the case_ids of this DeleteTestCaseInfo.

        用例id列表

        :return: The case_ids of this DeleteTestCaseInfo.
        :rtype: list[str]
        """
        return self._case_ids

    @case_ids.setter
    def case_ids(self, case_ids):
        """Sets the case_ids of this DeleteTestCaseInfo.

        用例id列表

        :param case_ids: The case_ids of this DeleteTestCaseInfo.
        :type case_ids: list[str]
        """
        self._case_ids = case_ids

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
        if not isinstance(other, DeleteTestCaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
