# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePrePaidPublicipRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publicip': 'CreatePrePaidPublicipOption',
        'bandwidth': 'CreatePublicipBandwidthOption',
        'extend_param': 'CreatePrePaidPublicipExtendParamOption',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'publicip': 'publicip',
        'bandwidth': 'bandwidth',
        'extend_param': 'extendParam',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, publicip=None, bandwidth=None, extend_param=None, enterprise_project_id=None):
        """CreatePrePaidPublicipRequestBody

        The model defined in huaweicloud sdk

        :param publicip: 
        :type publicip: :class:`huaweicloudsdkeip.v2.CreatePrePaidPublicipOption`
        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdkeip.v2.CreatePublicipBandwidthOption`
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkeip.v2.CreatePrePaidPublicipExtendParamOption`
        :param enterprise_project_id: 企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。  创建弹性公网IP时，给弹性公网IP绑定企业项目ID。  不指定该参数时，默认值是 0
        :type enterprise_project_id: str
        """
        
        

        self._publicip = None
        self._bandwidth = None
        self._extend_param = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.publicip = publicip
        self.bandwidth = bandwidth
        if extend_param is not None:
            self.extend_param = extend_param
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def publicip(self):
        """Gets the publicip of this CreatePrePaidPublicipRequestBody.

        :return: The publicip of this CreatePrePaidPublicipRequestBody.
        :rtype: :class:`huaweicloudsdkeip.v2.CreatePrePaidPublicipOption`
        """
        return self._publicip

    @publicip.setter
    def publicip(self, publicip):
        """Sets the publicip of this CreatePrePaidPublicipRequestBody.

        :param publicip: The publicip of this CreatePrePaidPublicipRequestBody.
        :type publicip: :class:`huaweicloudsdkeip.v2.CreatePrePaidPublicipOption`
        """
        self._publicip = publicip

    @property
    def bandwidth(self):
        """Gets the bandwidth of this CreatePrePaidPublicipRequestBody.

        :return: The bandwidth of this CreatePrePaidPublicipRequestBody.
        :rtype: :class:`huaweicloudsdkeip.v2.CreatePublicipBandwidthOption`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this CreatePrePaidPublicipRequestBody.

        :param bandwidth: The bandwidth of this CreatePrePaidPublicipRequestBody.
        :type bandwidth: :class:`huaweicloudsdkeip.v2.CreatePublicipBandwidthOption`
        """
        self._bandwidth = bandwidth

    @property
    def extend_param(self):
        """Gets the extend_param of this CreatePrePaidPublicipRequestBody.

        :return: The extend_param of this CreatePrePaidPublicipRequestBody.
        :rtype: :class:`huaweicloudsdkeip.v2.CreatePrePaidPublicipExtendParamOption`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this CreatePrePaidPublicipRequestBody.

        :param extend_param: The extend_param of this CreatePrePaidPublicipRequestBody.
        :type extend_param: :class:`huaweicloudsdkeip.v2.CreatePrePaidPublicipExtendParamOption`
        """
        self._extend_param = extend_param

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreatePrePaidPublicipRequestBody.

        企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。  创建弹性公网IP时，给弹性公网IP绑定企业项目ID。  不指定该参数时，默认值是 0

        :return: The enterprise_project_id of this CreatePrePaidPublicipRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreatePrePaidPublicipRequestBody.

        企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。  创建弹性公网IP时，给弹性公网IP绑定企业项目ID。  不指定该参数时，默认值是 0

        :param enterprise_project_id: The enterprise_project_id of this CreatePrePaidPublicipRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, CreatePrePaidPublicipRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
