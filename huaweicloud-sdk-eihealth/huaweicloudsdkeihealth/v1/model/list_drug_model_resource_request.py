# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDrugModelResourceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec_code': 'str',
        'status_list': 'list[str]',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'spec_code': 'spec_code',
        'status_list': 'status_list',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, spec_code=None, status_list=None, limit=None, offset=None):
        r"""ListDrugModelResourceRequest

        The model defined in huaweicloud sdk

        :param spec_code: **参数解释**： 规格编码。 **约束限制**： 不涉及 **取值范围**： 长度为[1-64]个字符。 **默认取值**： 不涉及 
        :type spec_code: str
        :param status_list: **参数解释**： 盘古药物分子大模型的订购状态。 **约束限制**： 数组数量范围[0-10]，数组元素仅支持Normal|Freeze|Deleted。 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type status_list: list[str]
        :param limit: **参数解释**： 限制量，单次查询总量。 **约束限制**： 不涉及 **取值范围**： 1-1000 **默认取值**： 100 
        :type limit: int
        :param offset: **参数解释**： 偏移量，查询起始偏移。 **约束限制**： 不涉及 **取值范围**： 0-100000000 **默认取值**： 0 
        :type offset: int
        """
        
        

        self._spec_code = None
        self._status_list = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if spec_code is not None:
            self.spec_code = spec_code
        if status_list is not None:
            self.status_list = status_list
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def spec_code(self):
        r"""Gets the spec_code of this ListDrugModelResourceRequest.

        **参数解释**： 规格编码。 **约束限制**： 不涉及 **取值范围**： 长度为[1-64]个字符。 **默认取值**： 不涉及 

        :return: The spec_code of this ListDrugModelResourceRequest.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this ListDrugModelResourceRequest.

        **参数解释**： 规格编码。 **约束限制**： 不涉及 **取值范围**： 长度为[1-64]个字符。 **默认取值**： 不涉及 

        :param spec_code: The spec_code of this ListDrugModelResourceRequest.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def status_list(self):
        r"""Gets the status_list of this ListDrugModelResourceRequest.

        **参数解释**： 盘古药物分子大模型的订购状态。 **约束限制**： 数组数量范围[0-10]，数组元素仅支持Normal|Freeze|Deleted。 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The status_list of this ListDrugModelResourceRequest.
        :rtype: list[str]
        """
        return self._status_list

    @status_list.setter
    def status_list(self, status_list):
        r"""Sets the status_list of this ListDrugModelResourceRequest.

        **参数解释**： 盘古药物分子大模型的订购状态。 **约束限制**： 数组数量范围[0-10]，数组元素仅支持Normal|Freeze|Deleted。 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param status_list: The status_list of this ListDrugModelResourceRequest.
        :type status_list: list[str]
        """
        self._status_list = status_list

    @property
    def limit(self):
        r"""Gets the limit of this ListDrugModelResourceRequest.

        **参数解释**： 限制量，单次查询总量。 **约束限制**： 不涉及 **取值范围**： 1-1000 **默认取值**： 100 

        :return: The limit of this ListDrugModelResourceRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDrugModelResourceRequest.

        **参数解释**： 限制量，单次查询总量。 **约束限制**： 不涉及 **取值范围**： 1-1000 **默认取值**： 100 

        :param limit: The limit of this ListDrugModelResourceRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListDrugModelResourceRequest.

        **参数解释**： 偏移量，查询起始偏移。 **约束限制**： 不涉及 **取值范围**： 0-100000000 **默认取值**： 0 

        :return: The offset of this ListDrugModelResourceRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDrugModelResourceRequest.

        **参数解释**： 偏移量，查询起始偏移。 **约束限制**： 不涉及 **取值范围**： 0-100000000 **默认取值**： 0 

        :param offset: The offset of this ListDrugModelResourceRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListDrugModelResourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
