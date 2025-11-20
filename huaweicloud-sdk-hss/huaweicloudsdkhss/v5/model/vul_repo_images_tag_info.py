# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulRepoImagesTagInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag_id': 'str',
        'tag_name': 'str',
        'size': 'int',
        'app_name': 'str'
    }

    attribute_map = {
        'tag_id': 'tag_id',
        'tag_name': 'tag_name',
        'size': 'size',
        'app_name': 'app_name'
    }

    def __init__(self, tag_id=None, tag_name=None, size=None, app_name=None):
        r"""VulRepoImagesTagInfo

        The model defined in huaweicloud sdk

        :param tag_id: **参数解释**: 版本id **取值范围**: 字符长度0-65535位 
        :type tag_id: str
        :param tag_name: **参数解释**: 版本名称 **取值范围**: 字符长度0-65535位 
        :type tag_name: str
        :param size: **参数解释**: 版本大小 **取值范围**: 最小值0，最大值2147483547 
        :type size: int
        :param app_name: **参数解释**: 版本app名称 **取值范围**: 字符长度0-65535位 
        :type app_name: str
        """
        
        

        self._tag_id = None
        self._tag_name = None
        self._size = None
        self._app_name = None
        self.discriminator = None

        if tag_id is not None:
            self.tag_id = tag_id
        if tag_name is not None:
            self.tag_name = tag_name
        if size is not None:
            self.size = size
        if app_name is not None:
            self.app_name = app_name

    @property
    def tag_id(self):
        r"""Gets the tag_id of this VulRepoImagesTagInfo.

        **参数解释**: 版本id **取值范围**: 字符长度0-65535位 

        :return: The tag_id of this VulRepoImagesTagInfo.
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        r"""Sets the tag_id of this VulRepoImagesTagInfo.

        **参数解释**: 版本id **取值范围**: 字符长度0-65535位 

        :param tag_id: The tag_id of this VulRepoImagesTagInfo.
        :type tag_id: str
        """
        self._tag_id = tag_id

    @property
    def tag_name(self):
        r"""Gets the tag_name of this VulRepoImagesTagInfo.

        **参数解释**: 版本名称 **取值范围**: 字符长度0-65535位 

        :return: The tag_name of this VulRepoImagesTagInfo.
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        r"""Sets the tag_name of this VulRepoImagesTagInfo.

        **参数解释**: 版本名称 **取值范围**: 字符长度0-65535位 

        :param tag_name: The tag_name of this VulRepoImagesTagInfo.
        :type tag_name: str
        """
        self._tag_name = tag_name

    @property
    def size(self):
        r"""Gets the size of this VulRepoImagesTagInfo.

        **参数解释**: 版本大小 **取值范围**: 最小值0，最大值2147483547 

        :return: The size of this VulRepoImagesTagInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this VulRepoImagesTagInfo.

        **参数解释**: 版本大小 **取值范围**: 最小值0，最大值2147483547 

        :param size: The size of this VulRepoImagesTagInfo.
        :type size: int
        """
        self._size = size

    @property
    def app_name(self):
        r"""Gets the app_name of this VulRepoImagesTagInfo.

        **参数解释**: 版本app名称 **取值范围**: 字符长度0-65535位 

        :return: The app_name of this VulRepoImagesTagInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this VulRepoImagesTagInfo.

        **参数解释**: 版本app名称 **取值范围**: 字符长度0-65535位 

        :param app_name: The app_name of this VulRepoImagesTagInfo.
        :type app_name: str
        """
        self._app_name = app_name

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
        if not isinstance(other, VulRepoImagesTagInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
