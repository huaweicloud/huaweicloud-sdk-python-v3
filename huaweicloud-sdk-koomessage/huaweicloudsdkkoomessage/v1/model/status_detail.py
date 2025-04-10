# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatusDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'carrier': 'str',
        'status': 'int',
        'desc': 'str'
    }

    attribute_map = {
        'carrier': 'carrier',
        'status': 'status',
        'desc': 'desc'
    }

    def __init__(self, carrier=None, status=None, desc=None):
        r"""StatusDetail

        The model defined in huaweicloud sdk

        :param carrier: 运营商类型。  - cmcc：中国移动 - cucc：中国联通 - ctcc：中国电信 - oversea：港澳台及国外 - unknown：未知 
        :type carrier: str
        :param status: 模板状态： - 0：正常可用  - 1：审核中  - 2：审核不通过  - 3：模板已禁用  - 4：模板不存在  - 5：模板已过期 
        :type status: int
        :param desc: 对模板状态的描述。  &gt; 若状态是审核不通过或被禁用，描述表示的是不通过或禁用的原因。 
        :type desc: str
        """
        
        

        self._carrier = None
        self._status = None
        self._desc = None
        self.discriminator = None

        if carrier is not None:
            self.carrier = carrier
        if status is not None:
            self.status = status
        if desc is not None:
            self.desc = desc

    @property
    def carrier(self):
        r"""Gets the carrier of this StatusDetail.

        运营商类型。  - cmcc：中国移动 - cucc：中国联通 - ctcc：中国电信 - oversea：港澳台及国外 - unknown：未知 

        :return: The carrier of this StatusDetail.
        :rtype: str
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        r"""Sets the carrier of this StatusDetail.

        运营商类型。  - cmcc：中国移动 - cucc：中国联通 - ctcc：中国电信 - oversea：港澳台及国外 - unknown：未知 

        :param carrier: The carrier of this StatusDetail.
        :type carrier: str
        """
        self._carrier = carrier

    @property
    def status(self):
        r"""Gets the status of this StatusDetail.

        模板状态： - 0：正常可用  - 1：审核中  - 2：审核不通过  - 3：模板已禁用  - 4：模板不存在  - 5：模板已过期 

        :return: The status of this StatusDetail.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StatusDetail.

        模板状态： - 0：正常可用  - 1：审核中  - 2：审核不通过  - 3：模板已禁用  - 4：模板不存在  - 5：模板已过期 

        :param status: The status of this StatusDetail.
        :type status: int
        """
        self._status = status

    @property
    def desc(self):
        r"""Gets the desc of this StatusDetail.

        对模板状态的描述。  > 若状态是审核不通过或被禁用，描述表示的是不通过或禁用的原因。 

        :return: The desc of this StatusDetail.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this StatusDetail.

        对模板状态的描述。  > 若状态是审核不通过或被禁用，描述表示的是不通过或禁用的原因。 

        :param desc: The desc of this StatusDetail.
        :type desc: str
        """
        self._desc = desc

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
        if not isinstance(other, StatusDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
