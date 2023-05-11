# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiagnosisDimension:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'abnormal_num': 'int',
        'failed_num': 'int',
        'diagnosis_item_list': 'list[DiagnosisItem]'
    }

    attribute_map = {
        'name': 'name',
        'abnormal_num': 'abnormal_num',
        'failed_num': 'failed_num',
        'diagnosis_item_list': 'diagnosis_item_list'
    }

    def __init__(self, name=None, abnormal_num=None, failed_num=None, diagnosis_item_list=None):
        """DiagnosisDimension

        The model defined in huaweicloud sdk

        :param name: 诊断维度名称
        :type name: str
        :param abnormal_num: 诊断结果为异常的诊断项总数
        :type abnormal_num: int
        :param failed_num: 诊断失败的诊断项总数
        :type failed_num: int
        :param diagnosis_item_list: 诊断项列表
        :type diagnosis_item_list: list[:class:`huaweicloudsdkdcs.v2.DiagnosisItem`]
        """
        
        

        self._name = None
        self._abnormal_num = None
        self._failed_num = None
        self._diagnosis_item_list = None
        self.discriminator = None

        self.name = name
        self.abnormal_num = abnormal_num
        self.failed_num = failed_num
        self.diagnosis_item_list = diagnosis_item_list

    @property
    def name(self):
        """Gets the name of this DiagnosisDimension.

        诊断维度名称

        :return: The name of this DiagnosisDimension.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DiagnosisDimension.

        诊断维度名称

        :param name: The name of this DiagnosisDimension.
        :type name: str
        """
        self._name = name

    @property
    def abnormal_num(self):
        """Gets the abnormal_num of this DiagnosisDimension.

        诊断结果为异常的诊断项总数

        :return: The abnormal_num of this DiagnosisDimension.
        :rtype: int
        """
        return self._abnormal_num

    @abnormal_num.setter
    def abnormal_num(self, abnormal_num):
        """Sets the abnormal_num of this DiagnosisDimension.

        诊断结果为异常的诊断项总数

        :param abnormal_num: The abnormal_num of this DiagnosisDimension.
        :type abnormal_num: int
        """
        self._abnormal_num = abnormal_num

    @property
    def failed_num(self):
        """Gets the failed_num of this DiagnosisDimension.

        诊断失败的诊断项总数

        :return: The failed_num of this DiagnosisDimension.
        :rtype: int
        """
        return self._failed_num

    @failed_num.setter
    def failed_num(self, failed_num):
        """Sets the failed_num of this DiagnosisDimension.

        诊断失败的诊断项总数

        :param failed_num: The failed_num of this DiagnosisDimension.
        :type failed_num: int
        """
        self._failed_num = failed_num

    @property
    def diagnosis_item_list(self):
        """Gets the diagnosis_item_list of this DiagnosisDimension.

        诊断项列表

        :return: The diagnosis_item_list of this DiagnosisDimension.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.DiagnosisItem`]
        """
        return self._diagnosis_item_list

    @diagnosis_item_list.setter
    def diagnosis_item_list(self, diagnosis_item_list):
        """Sets the diagnosis_item_list of this DiagnosisDimension.

        诊断项列表

        :param diagnosis_item_list: The diagnosis_item_list of this DiagnosisDimension.
        :type diagnosis_item_list: list[:class:`huaweicloudsdkdcs.v2.DiagnosisItem`]
        """
        self._diagnosis_item_list = diagnosis_item_list

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
        if not isinstance(other, DiagnosisDimension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
