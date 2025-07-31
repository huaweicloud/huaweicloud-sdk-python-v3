# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowImageAssetStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'local_num': 'int',
        'cicd_num': 'int',
        'registry_num': 'int'
    }

    attribute_map = {
        'local_num': 'local_num',
        'cicd_num': 'cicd_num',
        'registry_num': 'registry_num'
    }

    def __init__(self, local_num=None, cicd_num=None, registry_num=None):
        r"""ShowImageAssetStatisticsResponse

        The model defined in huaweicloud sdk

        :param local_num: **参数解释**: 本地镜像数量 **取值范围**: 最小值0，最大值65535 
        :type local_num: int
        :param cicd_num: **参数解释**: cicd镜像数量 **取值范围**: 最小值0，最大值65535 
        :type cicd_num: int
        :param registry_num: **参数解释**: 仓库镜像数量 **取值范围**: 最小值0，最大值65535 
        :type registry_num: int
        """
        
        super(ShowImageAssetStatisticsResponse, self).__init__()

        self._local_num = None
        self._cicd_num = None
        self._registry_num = None
        self.discriminator = None

        if local_num is not None:
            self.local_num = local_num
        if cicd_num is not None:
            self.cicd_num = cicd_num
        if registry_num is not None:
            self.registry_num = registry_num

    @property
    def local_num(self):
        r"""Gets the local_num of this ShowImageAssetStatisticsResponse.

        **参数解释**: 本地镜像数量 **取值范围**: 最小值0，最大值65535 

        :return: The local_num of this ShowImageAssetStatisticsResponse.
        :rtype: int
        """
        return self._local_num

    @local_num.setter
    def local_num(self, local_num):
        r"""Sets the local_num of this ShowImageAssetStatisticsResponse.

        **参数解释**: 本地镜像数量 **取值范围**: 最小值0，最大值65535 

        :param local_num: The local_num of this ShowImageAssetStatisticsResponse.
        :type local_num: int
        """
        self._local_num = local_num

    @property
    def cicd_num(self):
        r"""Gets the cicd_num of this ShowImageAssetStatisticsResponse.

        **参数解释**: cicd镜像数量 **取值范围**: 最小值0，最大值65535 

        :return: The cicd_num of this ShowImageAssetStatisticsResponse.
        :rtype: int
        """
        return self._cicd_num

    @cicd_num.setter
    def cicd_num(self, cicd_num):
        r"""Sets the cicd_num of this ShowImageAssetStatisticsResponse.

        **参数解释**: cicd镜像数量 **取值范围**: 最小值0，最大值65535 

        :param cicd_num: The cicd_num of this ShowImageAssetStatisticsResponse.
        :type cicd_num: int
        """
        self._cicd_num = cicd_num

    @property
    def registry_num(self):
        r"""Gets the registry_num of this ShowImageAssetStatisticsResponse.

        **参数解释**: 仓库镜像数量 **取值范围**: 最小值0，最大值65535 

        :return: The registry_num of this ShowImageAssetStatisticsResponse.
        :rtype: int
        """
        return self._registry_num

    @registry_num.setter
    def registry_num(self, registry_num):
        r"""Sets the registry_num of this ShowImageAssetStatisticsResponse.

        **参数解释**: 仓库镜像数量 **取值范围**: 最小值0，最大值65535 

        :param registry_num: The registry_num of this ShowImageAssetStatisticsResponse.
        :type registry_num: int
        """
        self._registry_num = registry_num

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
        if not isinstance(other, ShowImageAssetStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
