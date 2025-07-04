# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LtslogInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'id': 'str',
        'log_type': 'str',
        'log_desc': 'str',
        'access_url': 'str'
    }

    attribute_map = {
        'status': 'status',
        'id': 'id',
        'log_type': 'log_type',
        'log_desc': 'log_desc',
        'access_url': 'access_url'
    }

    def __init__(self, status=None, id=None, log_type=None, log_desc=None, access_url=None):
        r"""LtslogInfo

        The model defined in huaweicloud sdk

        :param status: **参数解释**： 配置状态。 **取值范围**： 不涉及。
        :type status: str
        :param id: **参数解释**： 日志ID。 **取值范围**： 不涉及。
        :type id: str
        :param log_type: **参数解释**： 日志类型。 **取值范围**： 不涉及。
        :type log_type: str
        :param log_desc: **参数解释**： 日志描述。 **取值范围**： 不涉及。
        :type log_desc: str
        :param access_url: **参数解释**： LTS日志访问URL。 **取值范围**： 不涉及。
        :type access_url: str
        """
        
        

        self._status = None
        self._id = None
        self._log_type = None
        self._log_desc = None
        self._access_url = None
        self.discriminator = None

        self.status = status
        self.id = id
        self.log_type = log_type
        self.log_desc = log_desc
        self.access_url = access_url

    @property
    def status(self):
        r"""Gets the status of this LtslogInfo.

        **参数解释**： 配置状态。 **取值范围**： 不涉及。

        :return: The status of this LtslogInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this LtslogInfo.

        **参数解释**： 配置状态。 **取值范围**： 不涉及。

        :param status: The status of this LtslogInfo.
        :type status: str
        """
        self._status = status

    @property
    def id(self):
        r"""Gets the id of this LtslogInfo.

        **参数解释**： 日志ID。 **取值范围**： 不涉及。

        :return: The id of this LtslogInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this LtslogInfo.

        **参数解释**： 日志ID。 **取值范围**： 不涉及。

        :param id: The id of this LtslogInfo.
        :type id: str
        """
        self._id = id

    @property
    def log_type(self):
        r"""Gets the log_type of this LtslogInfo.

        **参数解释**： 日志类型。 **取值范围**： 不涉及。

        :return: The log_type of this LtslogInfo.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        r"""Sets the log_type of this LtslogInfo.

        **参数解释**： 日志类型。 **取值范围**： 不涉及。

        :param log_type: The log_type of this LtslogInfo.
        :type log_type: str
        """
        self._log_type = log_type

    @property
    def log_desc(self):
        r"""Gets the log_desc of this LtslogInfo.

        **参数解释**： 日志描述。 **取值范围**： 不涉及。

        :return: The log_desc of this LtslogInfo.
        :rtype: str
        """
        return self._log_desc

    @log_desc.setter
    def log_desc(self, log_desc):
        r"""Sets the log_desc of this LtslogInfo.

        **参数解释**： 日志描述。 **取值范围**： 不涉及。

        :param log_desc: The log_desc of this LtslogInfo.
        :type log_desc: str
        """
        self._log_desc = log_desc

    @property
    def access_url(self):
        r"""Gets the access_url of this LtslogInfo.

        **参数解释**： LTS日志访问URL。 **取值范围**： 不涉及。

        :return: The access_url of this LtslogInfo.
        :rtype: str
        """
        return self._access_url

    @access_url.setter
    def access_url(self, access_url):
        r"""Sets the access_url of this LtslogInfo.

        **参数解释**： LTS日志访问URL。 **取值范围**： 不涉及。

        :param access_url: The access_url of this LtslogInfo.
        :type access_url: str
        """
        self._access_url = access_url

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
        if not isinstance(other, LtslogInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
