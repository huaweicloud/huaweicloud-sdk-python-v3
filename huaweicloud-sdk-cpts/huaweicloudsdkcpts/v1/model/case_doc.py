# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CaseDoc:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'label_names': 'list[str]',
        'preparation': 'str',
        'rank': 'int',
        'status_code': 'int',
        'steps': 'list[CaseDocSteps]'
    }

    attribute_map = {
        'description': 'description',
        'label_names': 'label_names',
        'preparation': 'preparation',
        'rank': 'rank',
        'status_code': 'status_code',
        'steps': 'steps'
    }

    def __init__(self, description=None, label_names=None, preparation=None, rank=None, status_code=None, steps=None):
        """CaseDoc

        The model defined in huaweicloud sdk

        :param description: 用例描述信息
        :type description: str
        :param label_names: 标签
        :type label_names: list[str]
        :param preparation: 前置条件
        :type preparation: str
        :param rank: 用例等级（0-L0；1-L1；2-L2；3-L3；4-L4；）
        :type rank: int
        :param status_code: 状态（0-新建；5-设计中；6-测试中；7-完成；）
        :type status_code: int
        :param steps: 测试步骤
        :type steps: list[:class:`huaweicloudsdkcpts.v1.CaseDocSteps`]
        """
        
        

        self._description = None
        self._label_names = None
        self._preparation = None
        self._rank = None
        self._status_code = None
        self._steps = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if label_names is not None:
            self.label_names = label_names
        if preparation is not None:
            self.preparation = preparation
        if rank is not None:
            self.rank = rank
        if status_code is not None:
            self.status_code = status_code
        if steps is not None:
            self.steps = steps

    @property
    def description(self):
        """Gets the description of this CaseDoc.

        用例描述信息

        :return: The description of this CaseDoc.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CaseDoc.

        用例描述信息

        :param description: The description of this CaseDoc.
        :type description: str
        """
        self._description = description

    @property
    def label_names(self):
        """Gets the label_names of this CaseDoc.

        标签

        :return: The label_names of this CaseDoc.
        :rtype: list[str]
        """
        return self._label_names

    @label_names.setter
    def label_names(self, label_names):
        """Sets the label_names of this CaseDoc.

        标签

        :param label_names: The label_names of this CaseDoc.
        :type label_names: list[str]
        """
        self._label_names = label_names

    @property
    def preparation(self):
        """Gets the preparation of this CaseDoc.

        前置条件

        :return: The preparation of this CaseDoc.
        :rtype: str
        """
        return self._preparation

    @preparation.setter
    def preparation(self, preparation):
        """Sets the preparation of this CaseDoc.

        前置条件

        :param preparation: The preparation of this CaseDoc.
        :type preparation: str
        """
        self._preparation = preparation

    @property
    def rank(self):
        """Gets the rank of this CaseDoc.

        用例等级（0-L0；1-L1；2-L2；3-L3；4-L4；）

        :return: The rank of this CaseDoc.
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this CaseDoc.

        用例等级（0-L0；1-L1；2-L2；3-L3；4-L4；）

        :param rank: The rank of this CaseDoc.
        :type rank: int
        """
        self._rank = rank

    @property
    def status_code(self):
        """Gets the status_code of this CaseDoc.

        状态（0-新建；5-设计中；6-测试中；7-完成；）

        :return: The status_code of this CaseDoc.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this CaseDoc.

        状态（0-新建；5-设计中；6-测试中；7-完成；）

        :param status_code: The status_code of this CaseDoc.
        :type status_code: int
        """
        self._status_code = status_code

    @property
    def steps(self):
        """Gets the steps of this CaseDoc.

        测试步骤

        :return: The steps of this CaseDoc.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.CaseDocSteps`]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this CaseDoc.

        测试步骤

        :param steps: The steps of this CaseDoc.
        :type steps: list[:class:`huaweicloudsdkcpts.v1.CaseDocSteps`]
        """
        self._steps = steps

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
        if not isinstance(other, CaseDoc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
