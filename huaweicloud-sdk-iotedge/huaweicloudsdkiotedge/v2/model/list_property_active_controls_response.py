# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPropertyActiveControlsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_id': 'str',
        'service_id': 'str',
        '_property': 'str',
        'active_controls': 'list[ActiveControlRspDTO]',
        'result_code': 'int',
        'result_desc': 'str'
    }

    attribute_map = {
        'device_id': 'device_id',
        'service_id': 'service_id',
        '_property': 'property',
        'active_controls': 'active_controls',
        'result_code': 'result_code',
        'result_desc': 'result_desc'
    }

    def __init__(self, device_id=None, service_id=None, _property=None, active_controls=None, result_code=None, result_desc=None):
        r"""ListPropertyActiveControlsResponse

        The model defined in huaweicloud sdk

        :param device_id: 设备id
        :type device_id: str
        :param service_id: 设备的服务id
        :type service_id: str
        :param _property: 设备的属性
        :type _property: str
        :param active_controls: 正在执行中的控制列表
        :type active_controls: list[:class:`huaweicloudsdkiotedge.v2.ActiveControlRspDTO`]
        :param result_code: 结果响应码，大于等于400表示失败，小于400表示成功
        :type result_code: int
        :param result_desc: 结果描述
        :type result_desc: str
        """
        
        super(ListPropertyActiveControlsResponse, self).__init__()

        self._device_id = None
        self._service_id = None
        self.__property = None
        self._active_controls = None
        self._result_code = None
        self._result_desc = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if service_id is not None:
            self.service_id = service_id
        if _property is not None:
            self._property = _property
        if active_controls is not None:
            self.active_controls = active_controls
        if result_code is not None:
            self.result_code = result_code
        if result_desc is not None:
            self.result_desc = result_desc

    @property
    def device_id(self):
        r"""Gets the device_id of this ListPropertyActiveControlsResponse.

        设备id

        :return: The device_id of this ListPropertyActiveControlsResponse.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this ListPropertyActiveControlsResponse.

        设备id

        :param device_id: The device_id of this ListPropertyActiveControlsResponse.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def service_id(self):
        r"""Gets the service_id of this ListPropertyActiveControlsResponse.

        设备的服务id

        :return: The service_id of this ListPropertyActiveControlsResponse.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this ListPropertyActiveControlsResponse.

        设备的服务id

        :param service_id: The service_id of this ListPropertyActiveControlsResponse.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def _property(self):
        r"""Gets the _property of this ListPropertyActiveControlsResponse.

        设备的属性

        :return: The _property of this ListPropertyActiveControlsResponse.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        r"""Sets the _property of this ListPropertyActiveControlsResponse.

        设备的属性

        :param _property: The _property of this ListPropertyActiveControlsResponse.
        :type _property: str
        """
        self.__property = _property

    @property
    def active_controls(self):
        r"""Gets the active_controls of this ListPropertyActiveControlsResponse.

        正在执行中的控制列表

        :return: The active_controls of this ListPropertyActiveControlsResponse.
        :rtype: list[:class:`huaweicloudsdkiotedge.v2.ActiveControlRspDTO`]
        """
        return self._active_controls

    @active_controls.setter
    def active_controls(self, active_controls):
        r"""Sets the active_controls of this ListPropertyActiveControlsResponse.

        正在执行中的控制列表

        :param active_controls: The active_controls of this ListPropertyActiveControlsResponse.
        :type active_controls: list[:class:`huaweicloudsdkiotedge.v2.ActiveControlRspDTO`]
        """
        self._active_controls = active_controls

    @property
    def result_code(self):
        r"""Gets the result_code of this ListPropertyActiveControlsResponse.

        结果响应码，大于等于400表示失败，小于400表示成功

        :return: The result_code of this ListPropertyActiveControlsResponse.
        :rtype: int
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        r"""Sets the result_code of this ListPropertyActiveControlsResponse.

        结果响应码，大于等于400表示失败，小于400表示成功

        :param result_code: The result_code of this ListPropertyActiveControlsResponse.
        :type result_code: int
        """
        self._result_code = result_code

    @property
    def result_desc(self):
        r"""Gets the result_desc of this ListPropertyActiveControlsResponse.

        结果描述

        :return: The result_desc of this ListPropertyActiveControlsResponse.
        :rtype: str
        """
        return self._result_desc

    @result_desc.setter
    def result_desc(self, result_desc):
        r"""Sets the result_desc of this ListPropertyActiveControlsResponse.

        结果描述

        :param result_desc: The result_desc of this ListPropertyActiveControlsResponse.
        :type result_desc: str
        """
        self._result_desc = result_desc

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
        if not isinstance(other, ListPropertyActiveControlsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
