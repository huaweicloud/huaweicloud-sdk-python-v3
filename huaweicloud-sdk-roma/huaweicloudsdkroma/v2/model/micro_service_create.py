# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MicroServiceCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_type': 'str',
        'cse_info': 'MicroServiceInfoCSEBase',
        'cce_info': 'MicroServiceInfoCCEBase'
    }

    attribute_map = {
        'service_type': 'service_type',
        'cse_info': 'cse_info',
        'cce_info': 'cce_info'
    }

    def __init__(self, service_type=None, cse_info=None, cce_info=None):
        r"""MicroServiceCreate

        The model defined in huaweicloud sdk

        :param service_type: 微服务类型： - CSE：CSE微服务注册中心 - CCE：CCE云容器引擎（暂不支持）
        :type service_type: str
        :param cse_info: 
        :type cse_info: :class:`huaweicloudsdkroma.v2.MicroServiceInfoCSEBase`
        :param cce_info: 
        :type cce_info: :class:`huaweicloudsdkroma.v2.MicroServiceInfoCCEBase`
        """
        
        

        self._service_type = None
        self._cse_info = None
        self._cce_info = None
        self.discriminator = None

        if service_type is not None:
            self.service_type = service_type
        if cse_info is not None:
            self.cse_info = cse_info
        if cce_info is not None:
            self.cce_info = cce_info

    @property
    def service_type(self):
        r"""Gets the service_type of this MicroServiceCreate.

        微服务类型： - CSE：CSE微服务注册中心 - CCE：CCE云容器引擎（暂不支持）

        :return: The service_type of this MicroServiceCreate.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this MicroServiceCreate.

        微服务类型： - CSE：CSE微服务注册中心 - CCE：CCE云容器引擎（暂不支持）

        :param service_type: The service_type of this MicroServiceCreate.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def cse_info(self):
        r"""Gets the cse_info of this MicroServiceCreate.

        :return: The cse_info of this MicroServiceCreate.
        :rtype: :class:`huaweicloudsdkroma.v2.MicroServiceInfoCSEBase`
        """
        return self._cse_info

    @cse_info.setter
    def cse_info(self, cse_info):
        r"""Sets the cse_info of this MicroServiceCreate.

        :param cse_info: The cse_info of this MicroServiceCreate.
        :type cse_info: :class:`huaweicloudsdkroma.v2.MicroServiceInfoCSEBase`
        """
        self._cse_info = cse_info

    @property
    def cce_info(self):
        r"""Gets the cce_info of this MicroServiceCreate.

        :return: The cce_info of this MicroServiceCreate.
        :rtype: :class:`huaweicloudsdkroma.v2.MicroServiceInfoCCEBase`
        """
        return self._cce_info

    @cce_info.setter
    def cce_info(self, cce_info):
        r"""Sets the cce_info of this MicroServiceCreate.

        :param cce_info: The cce_info of this MicroServiceCreate.
        :type cce_info: :class:`huaweicloudsdkroma.v2.MicroServiceInfoCCEBase`
        """
        self._cce_info = cce_info

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
        if not isinstance(other, MicroServiceCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
