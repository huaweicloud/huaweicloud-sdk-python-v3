# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DocumentVersionVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'version_uuid': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'version': 'version',
        'version_uuid': 'version_uuid',
        'create_time': 'create_time'
    }

    def __init__(self, version=None, version_uuid=None, create_time=None):
        r"""DocumentVersionVo

        The model defined in huaweicloud sdk

        :param version: 版本号，如v1
        :type version: str
        :param version_uuid: 版本id
        :type version_uuid: str
        :param create_time: 版本创建时间
        :type create_time: str
        """
        
        

        self._version = None
        self._version_uuid = None
        self._create_time = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if version_uuid is not None:
            self.version_uuid = version_uuid
        if create_time is not None:
            self.create_time = create_time

    @property
    def version(self):
        r"""Gets the version of this DocumentVersionVo.

        版本号，如v1

        :return: The version of this DocumentVersionVo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this DocumentVersionVo.

        版本号，如v1

        :param version: The version of this DocumentVersionVo.
        :type version: str
        """
        self._version = version

    @property
    def version_uuid(self):
        r"""Gets the version_uuid of this DocumentVersionVo.

        版本id

        :return: The version_uuid of this DocumentVersionVo.
        :rtype: str
        """
        return self._version_uuid

    @version_uuid.setter
    def version_uuid(self, version_uuid):
        r"""Sets the version_uuid of this DocumentVersionVo.

        版本id

        :param version_uuid: The version_uuid of this DocumentVersionVo.
        :type version_uuid: str
        """
        self._version_uuid = version_uuid

    @property
    def create_time(self):
        r"""Gets the create_time of this DocumentVersionVo.

        版本创建时间

        :return: The create_time of this DocumentVersionVo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DocumentVersionVo.

        版本创建时间

        :param create_time: The create_time of this DocumentVersionVo.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, DocumentVersionVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
