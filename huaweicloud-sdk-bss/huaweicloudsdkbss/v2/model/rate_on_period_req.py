# coding: utf-8

import pprint
import re

import six





class RateOnPeriodReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'product_infos': 'list[PeriodProductInfo]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'product_infos': 'product_infos'
    }

    def __init__(self, project_id=None, product_infos=None):
        """RateOnPeriodReq - a model defined in huaweicloud sdk"""
        
        

        self._project_id = None
        self._product_infos = None
        self.discriminator = None

        self.project_id = project_id
        self.product_infos = product_infos

    @property
    def project_id(self):
        """Gets the project_id of this RateOnPeriodReq.

        |参数名称：项目ID| |参数约束及描述：如果使用客户AK/SK或者Token，可以调用“通过assume_role方式获取用户token”接口获取“regionId”取值对应的project id。|

        :return: The project_id of this RateOnPeriodReq.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this RateOnPeriodReq.

        |参数名称：项目ID| |参数约束及描述：如果使用客户AK/SK或者Token，可以调用“通过assume_role方式获取用户token”接口获取“regionId”取值对应的project id。|

        :param project_id: The project_id of this RateOnPeriodReq.
        :type: str
        """
        self._project_id = project_id

    @property
    def product_infos(self):
        """Gets the product_infos of this RateOnPeriodReq.

        |参数名称：产品信息列表| |参数的约束及描述：询价时要询价产品的信息的列表|

        :return: The product_infos of this RateOnPeriodReq.
        :rtype: list[PeriodProductInfo]
        """
        return self._product_infos

    @product_infos.setter
    def product_infos(self, product_infos):
        """Sets the product_infos of this RateOnPeriodReq.

        |参数名称：产品信息列表| |参数的约束及描述：询价时要询价产品的信息的列表|

        :param product_infos: The product_infos of this RateOnPeriodReq.
        :type: list[PeriodProductInfo]
        """
        self._product_infos = product_infos

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
        if not isinstance(other, RateOnPeriodReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
