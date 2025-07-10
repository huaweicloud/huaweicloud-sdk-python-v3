# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BestPracticeCheckItemDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'check_item': 'int',
        'check_item_name': 'str',
        'risk_description': 'str',
        'result': 'str',
        'scene': 'str',
        'risk_level': 'str'
    }

    attribute_map = {
        'check_item': 'check_item',
        'check_item_name': 'check_item_name',
        'risk_description': 'risk_description',
        'result': 'result',
        'scene': 'scene',
        'risk_level': 'risk_level'
    }

    def __init__(self, check_item=None, check_item_name=None, risk_description=None, result=None, scene=None, risk_level=None):
        r"""BestPracticeCheckItemDetail

        The model defined in huaweicloud sdk

        :param check_item: 检查项编号
        :type check_item: int
        :param check_item_name: 检查项描述
        :type check_item_name: str
        :param risk_description: 检查项风险描述
        :type risk_description: str
        :param result: 检测结果
        :type result: str
        :param scene: 八大领域的细分场景
        :type scene: str
        :param risk_level: 风险等级
        :type risk_level: str
        """
        
        

        self._check_item = None
        self._check_item_name = None
        self._risk_description = None
        self._result = None
        self._scene = None
        self._risk_level = None
        self.discriminator = None

        if check_item is not None:
            self.check_item = check_item
        if check_item_name is not None:
            self.check_item_name = check_item_name
        if risk_description is not None:
            self.risk_description = risk_description
        if result is not None:
            self.result = result
        if scene is not None:
            self.scene = scene
        if risk_level is not None:
            self.risk_level = risk_level

    @property
    def check_item(self):
        r"""Gets the check_item of this BestPracticeCheckItemDetail.

        检查项编号

        :return: The check_item of this BestPracticeCheckItemDetail.
        :rtype: int
        """
        return self._check_item

    @check_item.setter
    def check_item(self, check_item):
        r"""Sets the check_item of this BestPracticeCheckItemDetail.

        检查项编号

        :param check_item: The check_item of this BestPracticeCheckItemDetail.
        :type check_item: int
        """
        self._check_item = check_item

    @property
    def check_item_name(self):
        r"""Gets the check_item_name of this BestPracticeCheckItemDetail.

        检查项描述

        :return: The check_item_name of this BestPracticeCheckItemDetail.
        :rtype: str
        """
        return self._check_item_name

    @check_item_name.setter
    def check_item_name(self, check_item_name):
        r"""Sets the check_item_name of this BestPracticeCheckItemDetail.

        检查项描述

        :param check_item_name: The check_item_name of this BestPracticeCheckItemDetail.
        :type check_item_name: str
        """
        self._check_item_name = check_item_name

    @property
    def risk_description(self):
        r"""Gets the risk_description of this BestPracticeCheckItemDetail.

        检查项风险描述

        :return: The risk_description of this BestPracticeCheckItemDetail.
        :rtype: str
        """
        return self._risk_description

    @risk_description.setter
    def risk_description(self, risk_description):
        r"""Sets the risk_description of this BestPracticeCheckItemDetail.

        检查项风险描述

        :param risk_description: The risk_description of this BestPracticeCheckItemDetail.
        :type risk_description: str
        """
        self._risk_description = risk_description

    @property
    def result(self):
        r"""Gets the result of this BestPracticeCheckItemDetail.

        检测结果

        :return: The result of this BestPracticeCheckItemDetail.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this BestPracticeCheckItemDetail.

        检测结果

        :param result: The result of this BestPracticeCheckItemDetail.
        :type result: str
        """
        self._result = result

    @property
    def scene(self):
        r"""Gets the scene of this BestPracticeCheckItemDetail.

        八大领域的细分场景

        :return: The scene of this BestPracticeCheckItemDetail.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        r"""Sets the scene of this BestPracticeCheckItemDetail.

        八大领域的细分场景

        :param scene: The scene of this BestPracticeCheckItemDetail.
        :type scene: str
        """
        self._scene = scene

    @property
    def risk_level(self):
        r"""Gets the risk_level of this BestPracticeCheckItemDetail.

        风险等级

        :return: The risk_level of this BestPracticeCheckItemDetail.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this BestPracticeCheckItemDetail.

        风险等级

        :param risk_level: The risk_level of this BestPracticeCheckItemDetail.
        :type risk_level: str
        """
        self._risk_level = risk_level

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
        if not isinstance(other, BestPracticeCheckItemDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
