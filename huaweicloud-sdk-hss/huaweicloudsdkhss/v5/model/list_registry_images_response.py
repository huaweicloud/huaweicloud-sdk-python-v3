# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRegistryImagesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'data_list': 'list[RegistryImagesInfo]'
    }

    attribute_map = {
        'total_num': 'total_num',
        'data_list': 'data_list'
    }

    def __init__(self, total_num=None, data_list=None):
        r"""ListRegistryImagesResponse

        The model defined in huaweicloud sdk

        :param total_num: **参数解释**: 满足查询条件的镜像记录总数量 **取值范围**: 0-2147483547；单位：个 
        :type total_num: int
        :param data_list: **参数解释**: 查询到的仓库镜像详细信息列表 **取值范围**: 数组长度0-当前查询的limit值（1-200），数组元素为RegistryImagesInfo对象 
        :type data_list: list[:class:`huaweicloudsdkhss.v5.RegistryImagesInfo`]
        """
        
        super().__init__()

        self._total_num = None
        self._data_list = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if data_list is not None:
            self.data_list = data_list

    @property
    def total_num(self):
        r"""Gets the total_num of this ListRegistryImagesResponse.

        **参数解释**: 满足查询条件的镜像记录总数量 **取值范围**: 0-2147483547；单位：个 

        :return: The total_num of this ListRegistryImagesResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ListRegistryImagesResponse.

        **参数解释**: 满足查询条件的镜像记录总数量 **取值范围**: 0-2147483547；单位：个 

        :param total_num: The total_num of this ListRegistryImagesResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def data_list(self):
        r"""Gets the data_list of this ListRegistryImagesResponse.

        **参数解释**: 查询到的仓库镜像详细信息列表 **取值范围**: 数组长度0-当前查询的limit值（1-200），数组元素为RegistryImagesInfo对象 

        :return: The data_list of this ListRegistryImagesResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.RegistryImagesInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ListRegistryImagesResponse.

        **参数解释**: 查询到的仓库镜像详细信息列表 **取值范围**: 数组长度0-当前查询的limit值（1-200），数组元素为RegistryImagesInfo对象 

        :param data_list: The data_list of this ListRegistryImagesResponse.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.RegistryImagesInfo`]
        """
        self._data_list = data_list

    def to_dict(self):
        import warnings
        warnings.warn("ListRegistryImagesResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListRegistryImagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
