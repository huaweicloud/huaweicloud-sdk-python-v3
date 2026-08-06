# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSupportedEnginesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'all_engine_types': 'list[str]',
        'supported_engine_types': 'list[str]',
        'supported_net_work_types': 'list[SupportNetWorkTypeResponse]',
        'supported_cloud_dba_types': 'list[SupportNetWorkTypeResponse]'
    }

    attribute_map = {
        'all_engine_types': 'all_engine_types',
        'supported_engine_types': 'supported_engine_types',
        'supported_net_work_types': 'supported_net_work_types',
        'supported_cloud_dba_types': 'supported_cloud_dba_types'
    }

    def __init__(self, all_engine_types=None, supported_engine_types=None, supported_net_work_types=None, supported_cloud_dba_types=None):
        r"""ShowSupportedEnginesResponse

        The model defined in huaweicloud sdk

        :param all_engine_types: 所有EngineType
        :type all_engine_types: list[str]
        :param supported_engine_types: 支持的EngineType
        :type supported_engine_types: list[str]
        :param supported_net_work_types: 支持的NetWorkType和EngineType
        :type supported_net_work_types: list[:class:`huaweicloudsdkdas.v3.SupportNetWorkTypeResponse`]
        :param supported_cloud_dba_types: 支持的CloudDBA的NetWorkType和EngineType
        :type supported_cloud_dba_types: list[:class:`huaweicloudsdkdas.v3.SupportNetWorkTypeResponse`]
        """
        
        super().__init__()

        self._all_engine_types = None
        self._supported_engine_types = None
        self._supported_net_work_types = None
        self._supported_cloud_dba_types = None
        self.discriminator = None

        if all_engine_types is not None:
            self.all_engine_types = all_engine_types
        if supported_engine_types is not None:
            self.supported_engine_types = supported_engine_types
        if supported_net_work_types is not None:
            self.supported_net_work_types = supported_net_work_types
        if supported_cloud_dba_types is not None:
            self.supported_cloud_dba_types = supported_cloud_dba_types

    @property
    def all_engine_types(self):
        r"""Gets the all_engine_types of this ShowSupportedEnginesResponse.

        所有EngineType

        :return: The all_engine_types of this ShowSupportedEnginesResponse.
        :rtype: list[str]
        """
        return self._all_engine_types

    @all_engine_types.setter
    def all_engine_types(self, all_engine_types):
        r"""Sets the all_engine_types of this ShowSupportedEnginesResponse.

        所有EngineType

        :param all_engine_types: The all_engine_types of this ShowSupportedEnginesResponse.
        :type all_engine_types: list[str]
        """
        self._all_engine_types = all_engine_types

    @property
    def supported_engine_types(self):
        r"""Gets the supported_engine_types of this ShowSupportedEnginesResponse.

        支持的EngineType

        :return: The supported_engine_types of this ShowSupportedEnginesResponse.
        :rtype: list[str]
        """
        return self._supported_engine_types

    @supported_engine_types.setter
    def supported_engine_types(self, supported_engine_types):
        r"""Sets the supported_engine_types of this ShowSupportedEnginesResponse.

        支持的EngineType

        :param supported_engine_types: The supported_engine_types of this ShowSupportedEnginesResponse.
        :type supported_engine_types: list[str]
        """
        self._supported_engine_types = supported_engine_types

    @property
    def supported_net_work_types(self):
        r"""Gets the supported_net_work_types of this ShowSupportedEnginesResponse.

        支持的NetWorkType和EngineType

        :return: The supported_net_work_types of this ShowSupportedEnginesResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SupportNetWorkTypeResponse`]
        """
        return self._supported_net_work_types

    @supported_net_work_types.setter
    def supported_net_work_types(self, supported_net_work_types):
        r"""Sets the supported_net_work_types of this ShowSupportedEnginesResponse.

        支持的NetWorkType和EngineType

        :param supported_net_work_types: The supported_net_work_types of this ShowSupportedEnginesResponse.
        :type supported_net_work_types: list[:class:`huaweicloudsdkdas.v3.SupportNetWorkTypeResponse`]
        """
        self._supported_net_work_types = supported_net_work_types

    @property
    def supported_cloud_dba_types(self):
        r"""Gets the supported_cloud_dba_types of this ShowSupportedEnginesResponse.

        支持的CloudDBA的NetWorkType和EngineType

        :return: The supported_cloud_dba_types of this ShowSupportedEnginesResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SupportNetWorkTypeResponse`]
        """
        return self._supported_cloud_dba_types

    @supported_cloud_dba_types.setter
    def supported_cloud_dba_types(self, supported_cloud_dba_types):
        r"""Sets the supported_cloud_dba_types of this ShowSupportedEnginesResponse.

        支持的CloudDBA的NetWorkType和EngineType

        :param supported_cloud_dba_types: The supported_cloud_dba_types of this ShowSupportedEnginesResponse.
        :type supported_cloud_dba_types: list[:class:`huaweicloudsdkdas.v3.SupportNetWorkTypeResponse`]
        """
        self._supported_cloud_dba_types = supported_cloud_dba_types

    def to_dict(self):
        import warnings
        warnings.warn("ShowSupportedEnginesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSupportedEnginesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
