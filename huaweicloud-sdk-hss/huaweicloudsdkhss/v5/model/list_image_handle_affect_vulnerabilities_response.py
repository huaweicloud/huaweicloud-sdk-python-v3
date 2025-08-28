# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageHandleAffectVulnerabilitiesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_vul_num': 'int',
        'vul_num': 'int',
        'image_num': 'int',
        'data_list': 'list[ImageVulResponseInfo]'
    }

    attribute_map = {
        'total_vul_num': 'total_vul_num',
        'vul_num': 'vul_num',
        'image_num': 'image_num',
        'data_list': 'data_list'
    }

    def __init__(self, total_vul_num=None, vul_num=None, image_num=None, data_list=None):
        r"""ListImageHandleAffectVulnerabilitiesResponse

        The model defined in huaweicloud sdk

        :param total_vul_num: **参数解释**: 镜像-漏洞总条数 **取值范围**: 最小值0，最大值2147483547 
        :type total_vul_num: int
        :param vul_num: **参数解释**: 漏洞个数 **取值范围**: 最小值0，最大值2147483547 
        :type vul_num: int
        :param image_num: **参数解释**: 镜像个数 **取值范围**: 最小值0，最大值2147483547 
        :type image_num: int
        :param data_list: **参数解释**: 镜像漏洞列表 **取值范围**: 最小值0，最大值5000 
        :type data_list: list[:class:`huaweicloudsdkhss.v5.ImageVulResponseInfo`]
        """
        
        super(ListImageHandleAffectVulnerabilitiesResponse, self).__init__()

        self._total_vul_num = None
        self._vul_num = None
        self._image_num = None
        self._data_list = None
        self.discriminator = None

        if total_vul_num is not None:
            self.total_vul_num = total_vul_num
        if vul_num is not None:
            self.vul_num = vul_num
        if image_num is not None:
            self.image_num = image_num
        if data_list is not None:
            self.data_list = data_list

    @property
    def total_vul_num(self):
        r"""Gets the total_vul_num of this ListImageHandleAffectVulnerabilitiesResponse.

        **参数解释**: 镜像-漏洞总条数 **取值范围**: 最小值0，最大值2147483547 

        :return: The total_vul_num of this ListImageHandleAffectVulnerabilitiesResponse.
        :rtype: int
        """
        return self._total_vul_num

    @total_vul_num.setter
    def total_vul_num(self, total_vul_num):
        r"""Sets the total_vul_num of this ListImageHandleAffectVulnerabilitiesResponse.

        **参数解释**: 镜像-漏洞总条数 **取值范围**: 最小值0，最大值2147483547 

        :param total_vul_num: The total_vul_num of this ListImageHandleAffectVulnerabilitiesResponse.
        :type total_vul_num: int
        """
        self._total_vul_num = total_vul_num

    @property
    def vul_num(self):
        r"""Gets the vul_num of this ListImageHandleAffectVulnerabilitiesResponse.

        **参数解释**: 漏洞个数 **取值范围**: 最小值0，最大值2147483547 

        :return: The vul_num of this ListImageHandleAffectVulnerabilitiesResponse.
        :rtype: int
        """
        return self._vul_num

    @vul_num.setter
    def vul_num(self, vul_num):
        r"""Sets the vul_num of this ListImageHandleAffectVulnerabilitiesResponse.

        **参数解释**: 漏洞个数 **取值范围**: 最小值0，最大值2147483547 

        :param vul_num: The vul_num of this ListImageHandleAffectVulnerabilitiesResponse.
        :type vul_num: int
        """
        self._vul_num = vul_num

    @property
    def image_num(self):
        r"""Gets the image_num of this ListImageHandleAffectVulnerabilitiesResponse.

        **参数解释**: 镜像个数 **取值范围**: 最小值0，最大值2147483547 

        :return: The image_num of this ListImageHandleAffectVulnerabilitiesResponse.
        :rtype: int
        """
        return self._image_num

    @image_num.setter
    def image_num(self, image_num):
        r"""Sets the image_num of this ListImageHandleAffectVulnerabilitiesResponse.

        **参数解释**: 镜像个数 **取值范围**: 最小值0，最大值2147483547 

        :param image_num: The image_num of this ListImageHandleAffectVulnerabilitiesResponse.
        :type image_num: int
        """
        self._image_num = image_num

    @property
    def data_list(self):
        r"""Gets the data_list of this ListImageHandleAffectVulnerabilitiesResponse.

        **参数解释**: 镜像漏洞列表 **取值范围**: 最小值0，最大值5000 

        :return: The data_list of this ListImageHandleAffectVulnerabilitiesResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ImageVulResponseInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ListImageHandleAffectVulnerabilitiesResponse.

        **参数解释**: 镜像漏洞列表 **取值范围**: 最小值0，最大值5000 

        :param data_list: The data_list of this ListImageHandleAffectVulnerabilitiesResponse.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.ImageVulResponseInfo`]
        """
        self._data_list = data_list

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
        if not isinstance(other, ListImageHandleAffectVulnerabilitiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
