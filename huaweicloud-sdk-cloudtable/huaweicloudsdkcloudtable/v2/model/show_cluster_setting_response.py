# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterSettingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parm_status': 'int',
        'parameter_info': 'list[ParameterInfo]'
    }

    attribute_map = {
        'parm_status': 'parm_status',
        'parameter_info': 'parameter_info'
    }

    def __init__(self, parm_status=None, parameter_info=None):
        """ShowClusterSettingResponse

        The model defined in huaweicloud sdk

        :param parm_status: 集群参数生效状态：0、未更改 1、未应用 2、应用中 3、已应用 4、应用失败
        :type parm_status: int
        :param parameter_info: 参数列表
        :type parameter_info: list[:class:`huaweicloudsdkcloudtable.v2.ParameterInfo`]
        """
        
        super(ShowClusterSettingResponse, self).__init__()

        self._parm_status = None
        self._parameter_info = None
        self.discriminator = None

        if parm_status is not None:
            self.parm_status = parm_status
        if parameter_info is not None:
            self.parameter_info = parameter_info

    @property
    def parm_status(self):
        """Gets the parm_status of this ShowClusterSettingResponse.

        集群参数生效状态：0、未更改 1、未应用 2、应用中 3、已应用 4、应用失败

        :return: The parm_status of this ShowClusterSettingResponse.
        :rtype: int
        """
        return self._parm_status

    @parm_status.setter
    def parm_status(self, parm_status):
        """Sets the parm_status of this ShowClusterSettingResponse.

        集群参数生效状态：0、未更改 1、未应用 2、应用中 3、已应用 4、应用失败

        :param parm_status: The parm_status of this ShowClusterSettingResponse.
        :type parm_status: int
        """
        self._parm_status = parm_status

    @property
    def parameter_info(self):
        """Gets the parameter_info of this ShowClusterSettingResponse.

        参数列表

        :return: The parameter_info of this ShowClusterSettingResponse.
        :rtype: list[:class:`huaweicloudsdkcloudtable.v2.ParameterInfo`]
        """
        return self._parameter_info

    @parameter_info.setter
    def parameter_info(self, parameter_info):
        """Sets the parameter_info of this ShowClusterSettingResponse.

        参数列表

        :param parameter_info: The parameter_info of this ShowClusterSettingResponse.
        :type parameter_info: list[:class:`huaweicloudsdkcloudtable.v2.ParameterInfo`]
        """
        self._parameter_info = parameter_info

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
        if not isinstance(other, ShowClusterSettingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
