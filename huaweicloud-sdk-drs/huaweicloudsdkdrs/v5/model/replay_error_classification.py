# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplayErrorClassification:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_name': 'str',
        'error_type': 'str',
        'error_cnt': 'str',
        'error_template_cnt': 'str'
    }

    attribute_map = {
        'target_name': 'target_name',
        'error_type': 'error_type',
        'error_cnt': 'error_cnt',
        'error_template_cnt': 'error_template_cnt'
    }

    def __init__(self, target_name=None, error_type=None, error_cnt=None, error_template_cnt=None):
        r"""ReplayErrorClassification

        The model defined in huaweicloud sdk

        :param target_name: 目标库标识
        :type target_name: str
        :param error_type: 异常SQL分类
        :type error_type: str
        :param error_cnt: 异常SQL数量
        :type error_cnt: str
        :param error_template_cnt: 异常SQL模板数量
        :type error_template_cnt: str
        """
        
        

        self._target_name = None
        self._error_type = None
        self._error_cnt = None
        self._error_template_cnt = None
        self.discriminator = None

        if target_name is not None:
            self.target_name = target_name
        self.error_type = error_type
        if error_cnt is not None:
            self.error_cnt = error_cnt
        if error_template_cnt is not None:
            self.error_template_cnt = error_template_cnt

    @property
    def target_name(self):
        r"""Gets the target_name of this ReplayErrorClassification.

        目标库标识

        :return: The target_name of this ReplayErrorClassification.
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        r"""Sets the target_name of this ReplayErrorClassification.

        目标库标识

        :param target_name: The target_name of this ReplayErrorClassification.
        :type target_name: str
        """
        self._target_name = target_name

    @property
    def error_type(self):
        r"""Gets the error_type of this ReplayErrorClassification.

        异常SQL分类

        :return: The error_type of this ReplayErrorClassification.
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        r"""Sets the error_type of this ReplayErrorClassification.

        异常SQL分类

        :param error_type: The error_type of this ReplayErrorClassification.
        :type error_type: str
        """
        self._error_type = error_type

    @property
    def error_cnt(self):
        r"""Gets the error_cnt of this ReplayErrorClassification.

        异常SQL数量

        :return: The error_cnt of this ReplayErrorClassification.
        :rtype: str
        """
        return self._error_cnt

    @error_cnt.setter
    def error_cnt(self, error_cnt):
        r"""Sets the error_cnt of this ReplayErrorClassification.

        异常SQL数量

        :param error_cnt: The error_cnt of this ReplayErrorClassification.
        :type error_cnt: str
        """
        self._error_cnt = error_cnt

    @property
    def error_template_cnt(self):
        r"""Gets the error_template_cnt of this ReplayErrorClassification.

        异常SQL模板数量

        :return: The error_template_cnt of this ReplayErrorClassification.
        :rtype: str
        """
        return self._error_template_cnt

    @error_template_cnt.setter
    def error_template_cnt(self, error_template_cnt):
        r"""Sets the error_template_cnt of this ReplayErrorClassification.

        异常SQL模板数量

        :param error_template_cnt: The error_template_cnt of this ReplayErrorClassification.
        :type error_template_cnt: str
        """
        self._error_template_cnt = error_template_cnt

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
        if not isinstance(other, ReplayErrorClassification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
