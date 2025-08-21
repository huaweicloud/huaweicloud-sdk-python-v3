# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeployKeyDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'title': 'str',
        'fingerprint': 'str',
        'created_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'fingerprint': 'fingerprint',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, title=None, fingerprint=None, created_at=None):
        r"""DeployKeyDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 部署密钥ID。
        :type id: int
        :param title: **参数解释：** 部署密钥标题。
        :type title: str
        :param fingerprint: **参数解释：** 部署密钥指纹。
        :type fingerprint: str
        :param created_at: **参数解释：** 创建时间。
        :type created_at: str
        """
        
        

        self._id = None
        self._title = None
        self._fingerprint = None
        self._created_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        r"""Gets the id of this DeployKeyDto.

        **参数解释：** 部署密钥ID。

        :return: The id of this DeployKeyDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DeployKeyDto.

        **参数解释：** 部署密钥ID。

        :param id: The id of this DeployKeyDto.
        :type id: int
        """
        self._id = id

    @property
    def title(self):
        r"""Gets the title of this DeployKeyDto.

        **参数解释：** 部署密钥标题。

        :return: The title of this DeployKeyDto.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this DeployKeyDto.

        **参数解释：** 部署密钥标题。

        :param title: The title of this DeployKeyDto.
        :type title: str
        """
        self._title = title

    @property
    def fingerprint(self):
        r"""Gets the fingerprint of this DeployKeyDto.

        **参数解释：** 部署密钥指纹。

        :return: The fingerprint of this DeployKeyDto.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        r"""Sets the fingerprint of this DeployKeyDto.

        **参数解释：** 部署密钥指纹。

        :param fingerprint: The fingerprint of this DeployKeyDto.
        :type fingerprint: str
        """
        self._fingerprint = fingerprint

    @property
    def created_at(self):
        r"""Gets the created_at of this DeployKeyDto.

        **参数解释：** 创建时间。

        :return: The created_at of this DeployKeyDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this DeployKeyDto.

        **参数解释：** 创建时间。

        :param created_at: The created_at of this DeployKeyDto.
        :type created_at: str
        """
        self._created_at = created_at

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
        if not isinstance(other, DeployKeyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
