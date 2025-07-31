# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CicdConfigurationsResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cicd_id': 'str',
        'cicd_name': 'str',
        'associated_images_num': 'int',
        'associated_config_num': 'int'
    }

    attribute_map = {
        'cicd_id': 'cicd_id',
        'cicd_name': 'cicd_name',
        'associated_images_num': 'associated_images_num',
        'associated_config_num': 'associated_config_num'
    }

    def __init__(self, cicd_id=None, cicd_name=None, associated_images_num=None, associated_config_num=None):
        r"""CicdConfigurationsResponseInfo

        The model defined in huaweicloud sdk

        :param cicd_id: **参数解释** CI/CD标识 **约束限制** 不涉及 **取值范围** 字符长度0-128位  **默认取值** 不涉及
        :type cicd_id: str
        :param cicd_name: **参数解释** CI/CD名称 **约束限制** 不涉及 **取值范围** 字符长度0-128位  **默认取值** 不涉及
        :type cicd_name: str
        :param associated_images_num: **参数解释** 关联镜像扫描数量 **约束限制** 不涉及 **取值范围** 最小值0，最大值2147483647  **默认取值** 不涉及
        :type associated_images_num: int
        :param associated_config_num: **参数解释** 关联配置扫描数量 **约束限制** 不涉及 **取值范围** 最小值0，最大值2147483647  **默认取值** 不涉及
        :type associated_config_num: int
        """
        
        

        self._cicd_id = None
        self._cicd_name = None
        self._associated_images_num = None
        self._associated_config_num = None
        self.discriminator = None

        if cicd_id is not None:
            self.cicd_id = cicd_id
        if cicd_name is not None:
            self.cicd_name = cicd_name
        if associated_images_num is not None:
            self.associated_images_num = associated_images_num
        if associated_config_num is not None:
            self.associated_config_num = associated_config_num

    @property
    def cicd_id(self):
        r"""Gets the cicd_id of this CicdConfigurationsResponseInfo.

        **参数解释** CI/CD标识 **约束限制** 不涉及 **取值范围** 字符长度0-128位  **默认取值** 不涉及

        :return: The cicd_id of this CicdConfigurationsResponseInfo.
        :rtype: str
        """
        return self._cicd_id

    @cicd_id.setter
    def cicd_id(self, cicd_id):
        r"""Sets the cicd_id of this CicdConfigurationsResponseInfo.

        **参数解释** CI/CD标识 **约束限制** 不涉及 **取值范围** 字符长度0-128位  **默认取值** 不涉及

        :param cicd_id: The cicd_id of this CicdConfigurationsResponseInfo.
        :type cicd_id: str
        """
        self._cicd_id = cicd_id

    @property
    def cicd_name(self):
        r"""Gets the cicd_name of this CicdConfigurationsResponseInfo.

        **参数解释** CI/CD名称 **约束限制** 不涉及 **取值范围** 字符长度0-128位  **默认取值** 不涉及

        :return: The cicd_name of this CicdConfigurationsResponseInfo.
        :rtype: str
        """
        return self._cicd_name

    @cicd_name.setter
    def cicd_name(self, cicd_name):
        r"""Sets the cicd_name of this CicdConfigurationsResponseInfo.

        **参数解释** CI/CD名称 **约束限制** 不涉及 **取值范围** 字符长度0-128位  **默认取值** 不涉及

        :param cicd_name: The cicd_name of this CicdConfigurationsResponseInfo.
        :type cicd_name: str
        """
        self._cicd_name = cicd_name

    @property
    def associated_images_num(self):
        r"""Gets the associated_images_num of this CicdConfigurationsResponseInfo.

        **参数解释** 关联镜像扫描数量 **约束限制** 不涉及 **取值范围** 最小值0，最大值2147483647  **默认取值** 不涉及

        :return: The associated_images_num of this CicdConfigurationsResponseInfo.
        :rtype: int
        """
        return self._associated_images_num

    @associated_images_num.setter
    def associated_images_num(self, associated_images_num):
        r"""Sets the associated_images_num of this CicdConfigurationsResponseInfo.

        **参数解释** 关联镜像扫描数量 **约束限制** 不涉及 **取值范围** 最小值0，最大值2147483647  **默认取值** 不涉及

        :param associated_images_num: The associated_images_num of this CicdConfigurationsResponseInfo.
        :type associated_images_num: int
        """
        self._associated_images_num = associated_images_num

    @property
    def associated_config_num(self):
        r"""Gets the associated_config_num of this CicdConfigurationsResponseInfo.

        **参数解释** 关联配置扫描数量 **约束限制** 不涉及 **取值范围** 最小值0，最大值2147483647  **默认取值** 不涉及

        :return: The associated_config_num of this CicdConfigurationsResponseInfo.
        :rtype: int
        """
        return self._associated_config_num

    @associated_config_num.setter
    def associated_config_num(self, associated_config_num):
        r"""Sets the associated_config_num of this CicdConfigurationsResponseInfo.

        **参数解释** 关联配置扫描数量 **约束限制** 不涉及 **取值范围** 最小值0，最大值2147483647  **默认取值** 不涉及

        :param associated_config_num: The associated_config_num of this CicdConfigurationsResponseInfo.
        :type associated_config_num: int
        """
        self._associated_config_num = associated_config_num

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
        if not isinstance(other, CicdConfigurationsResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
