# coding: utf-8

import pprint
import re

import six





class QueryDeviceTypeResultDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'model': 'str',
        'enable_active_code': 'bool',
        'resolution': 'str',
        'support_projection_code': 'bool',
        'support_svc': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'model': 'model',
        'enable_active_code': 'enableActiveCode',
        'resolution': 'resolution',
        'support_projection_code': 'supportProjectionCode',
        'support_svc': 'supportSVC'
    }

    def __init__(self, type=None, model=None, enable_active_code=None, resolution=None, support_projection_code=None, support_svc=None):
        """QueryDeviceTypeResultDTO - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._model = None
        self._enable_active_code = None
        self._resolution = None
        self._support_projection_code = None
        self._support_svc = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if model is not None:
            self.model = model
        if enable_active_code is not None:
            self.enable_active_code = enable_active_code
        if resolution is not None:
            self.resolution = resolution
        if support_projection_code is not None:
            self.support_projection_code = support_projection_code
        if support_svc is not None:
            self.support_svc = support_svc

    @property
    def type(self):
        """Gets the type of this QueryDeviceTypeResultDTO.

        终端类型，区分自研和第三方终端

        :return: The type of this QueryDeviceTypeResultDTO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QueryDeviceTypeResultDTO.

        终端类型，区分自研和第三方终端

        :param type: The type of this QueryDeviceTypeResultDTO.
        :type: str
        """
        self._type = type

    @property
    def model(self):
        """Gets the model of this QueryDeviceTypeResultDTO.

        终端型号，枚举类型。当前支持TE系列硬件终端，具体的终端类型可以通过获取所有终端类型接口查询。

        :return: The model of this QueryDeviceTypeResultDTO.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this QueryDeviceTypeResultDTO.

        终端型号，枚举类型。当前支持TE系列硬件终端，具体的终端类型可以通过获取所有终端类型接口查询。

        :param model: The model of this QueryDeviceTypeResultDTO.
        :type: str
        """
        self._model = model

    @property
    def enable_active_code(self):
        """Gets the enable_active_code of this QueryDeviceTypeResultDTO.

        是否支持激活码

        :return: The enable_active_code of this QueryDeviceTypeResultDTO.
        :rtype: bool
        """
        return self._enable_active_code

    @enable_active_code.setter
    def enable_active_code(self, enable_active_code):
        """Sets the enable_active_code of this QueryDeviceTypeResultDTO.

        是否支持激活码

        :param enable_active_code: The enable_active_code of this QueryDeviceTypeResultDTO.
        :type: bool
        """
        self._enable_active_code = enable_active_code

    @property
    def resolution(self):
        """Gets the resolution of this QueryDeviceTypeResultDTO.

        屏幕分辨率。1080P、720P等。

        :return: The resolution of this QueryDeviceTypeResultDTO.
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this QueryDeviceTypeResultDTO.

        屏幕分辨率。1080P、720P等。

        :param resolution: The resolution of this QueryDeviceTypeResultDTO.
        :type: str
        """
        self._resolution = resolution

    @property
    def support_projection_code(self):
        """Gets the support_projection_code of this QueryDeviceTypeResultDTO.

        是否支持投影码

        :return: The support_projection_code of this QueryDeviceTypeResultDTO.
        :rtype: bool
        """
        return self._support_projection_code

    @support_projection_code.setter
    def support_projection_code(self, support_projection_code):
        """Sets the support_projection_code of this QueryDeviceTypeResultDTO.

        是否支持投影码

        :param support_projection_code: The support_projection_code of this QueryDeviceTypeResultDTO.
        :type: bool
        """
        self._support_projection_code = support_projection_code

    @property
    def support_svc(self):
        """Gets the support_svc of this QueryDeviceTypeResultDTO.

        是否支持SVC

        :return: The support_svc of this QueryDeviceTypeResultDTO.
        :rtype: bool
        """
        return self._support_svc

    @support_svc.setter
    def support_svc(self, support_svc):
        """Sets the support_svc of this QueryDeviceTypeResultDTO.

        是否支持SVC

        :param support_svc: The support_svc of this QueryDeviceTypeResultDTO.
        :type: bool
        """
        self._support_svc = support_svc

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QueryDeviceTypeResultDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
