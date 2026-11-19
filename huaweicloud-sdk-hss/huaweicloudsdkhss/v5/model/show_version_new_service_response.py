# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVersionNewServiceResponse(SdkResponse):

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
        'container_version': 'str'
    }

    attribute_map = {
        'version': 'version',
        'container_version': 'container_version'
    }

    def __init__(self, version=None, container_version=None):
        r"""ShowVersionNewServiceResponse

        The model defined in huaweicloud sdk

        :param version: **参数解释**: 租户最高主机版本 **取值范围**: - hss.version.basic：基础版 - hss.version.advanced：高级版 - hss.version.enterprise：企业版 - hss.version.premium：旗舰版 - hss.version.wtp：网页防篡改版 
        :type version: str
        :param container_version: **参数解释**: 租户最高容器版本 **取值范围**: - hss.version.container：容器版 
        :type container_version: str
        """
        
        super().__init__()

        self._version = None
        self._container_version = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if container_version is not None:
            self.container_version = container_version

    @property
    def version(self):
        r"""Gets the version of this ShowVersionNewServiceResponse.

        **参数解释**: 租户最高主机版本 **取值范围**: - hss.version.basic：基础版 - hss.version.advanced：高级版 - hss.version.enterprise：企业版 - hss.version.premium：旗舰版 - hss.version.wtp：网页防篡改版 

        :return: The version of this ShowVersionNewServiceResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowVersionNewServiceResponse.

        **参数解释**: 租户最高主机版本 **取值范围**: - hss.version.basic：基础版 - hss.version.advanced：高级版 - hss.version.enterprise：企业版 - hss.version.premium：旗舰版 - hss.version.wtp：网页防篡改版 

        :param version: The version of this ShowVersionNewServiceResponse.
        :type version: str
        """
        self._version = version

    @property
    def container_version(self):
        r"""Gets the container_version of this ShowVersionNewServiceResponse.

        **参数解释**: 租户最高容器版本 **取值范围**: - hss.version.container：容器版 

        :return: The container_version of this ShowVersionNewServiceResponse.
        :rtype: str
        """
        return self._container_version

    @container_version.setter
    def container_version(self, container_version):
        r"""Sets the container_version of this ShowVersionNewServiceResponse.

        **参数解释**: 租户最高容器版本 **取值范围**: - hss.version.container：容器版 

        :param container_version: The container_version of this ShowVersionNewServiceResponse.
        :type container_version: str
        """
        self._container_version = container_version

    def to_dict(self):
        import warnings
        warnings.warn("ShowVersionNewServiceResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowVersionNewServiceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
