# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WiseBrainConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role_id': 'str',
        'sis_region': 'int',
        'sis_project_id': 'str',
        'enable_hot_words': 'bool'
    }

    attribute_map = {
        'role_id': 'role_id',
        'sis_region': 'sis_region',
        'sis_project_id': 'sis_project_id',
        'enable_hot_words': 'enable_hot_words'
    }

    def __init__(self, role_id=None, sis_region=None, sis_project_id=None, enable_hot_words=None):
        r"""WiseBrainConfig

        The model defined in huaweicloud sdk

        :param role_id: 角色ID。
        :type role_id: str
        :param sis_region: SIS所在区域
        :type sis_region: int
        :param sis_project_id: SIS所在区域的projectId
        :type sis_project_id: str
        :param enable_hot_words: 是否开启热词
        :type enable_hot_words: bool
        """
        
        

        self._role_id = None
        self._sis_region = None
        self._sis_project_id = None
        self._enable_hot_words = None
        self.discriminator = None

        if role_id is not None:
            self.role_id = role_id
        if sis_region is not None:
            self.sis_region = sis_region
        if sis_project_id is not None:
            self.sis_project_id = sis_project_id
        if enable_hot_words is not None:
            self.enable_hot_words = enable_hot_words

    @property
    def role_id(self):
        r"""Gets the role_id of this WiseBrainConfig.

        角色ID。

        :return: The role_id of this WiseBrainConfig.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this WiseBrainConfig.

        角色ID。

        :param role_id: The role_id of this WiseBrainConfig.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def sis_region(self):
        r"""Gets the sis_region of this WiseBrainConfig.

        SIS所在区域

        :return: The sis_region of this WiseBrainConfig.
        :rtype: int
        """
        return self._sis_region

    @sis_region.setter
    def sis_region(self, sis_region):
        r"""Sets the sis_region of this WiseBrainConfig.

        SIS所在区域

        :param sis_region: The sis_region of this WiseBrainConfig.
        :type sis_region: int
        """
        self._sis_region = sis_region

    @property
    def sis_project_id(self):
        r"""Gets the sis_project_id of this WiseBrainConfig.

        SIS所在区域的projectId

        :return: The sis_project_id of this WiseBrainConfig.
        :rtype: str
        """
        return self._sis_project_id

    @sis_project_id.setter
    def sis_project_id(self, sis_project_id):
        r"""Sets the sis_project_id of this WiseBrainConfig.

        SIS所在区域的projectId

        :param sis_project_id: The sis_project_id of this WiseBrainConfig.
        :type sis_project_id: str
        """
        self._sis_project_id = sis_project_id

    @property
    def enable_hot_words(self):
        r"""Gets the enable_hot_words of this WiseBrainConfig.

        是否开启热词

        :return: The enable_hot_words of this WiseBrainConfig.
        :rtype: bool
        """
        return self._enable_hot_words

    @enable_hot_words.setter
    def enable_hot_words(self, enable_hot_words):
        r"""Sets the enable_hot_words of this WiseBrainConfig.

        是否开启热词

        :param enable_hot_words: The enable_hot_words of this WiseBrainConfig.
        :type enable_hot_words: bool
        """
        self._enable_hot_words = enable_hot_words

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
        if not isinstance(other, WiseBrainConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
