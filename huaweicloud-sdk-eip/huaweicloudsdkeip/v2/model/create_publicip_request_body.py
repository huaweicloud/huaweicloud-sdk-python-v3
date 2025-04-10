# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePublicipRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth': 'CreatePublicipBandwidthOption',
        'enterprise_project_id': 'str',
        'publicip': 'CreatePublicipOption'
    }

    attribute_map = {
        'bandwidth': 'bandwidth',
        'enterprise_project_id': 'enterprise_project_id',
        'publicip': 'publicip'
    }

    def __init__(self, bandwidth=None, enterprise_project_id=None, publicip=None):
        r"""CreatePublicipRequestBody

        The model defined in huaweicloud sdk

        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdkeip.v2.CreatePublicipBandwidthOption`
        :param enterprise_project_id: 企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。  创建弹性公网IP时，给弹性公网IP绑定企业项目ID。  不指定该参数时，默认值是 0
        :type enterprise_project_id: str
        :param publicip: 
        :type publicip: :class:`huaweicloudsdkeip.v2.CreatePublicipOption`
        """
        
        

        self._bandwidth = None
        self._enterprise_project_id = None
        self._publicip = None
        self.discriminator = None

        self.bandwidth = bandwidth
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.publicip = publicip

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this CreatePublicipRequestBody.

        :return: The bandwidth of this CreatePublicipRequestBody.
        :rtype: :class:`huaweicloudsdkeip.v2.CreatePublicipBandwidthOption`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this CreatePublicipRequestBody.

        :param bandwidth: The bandwidth of this CreatePublicipRequestBody.
        :type bandwidth: :class:`huaweicloudsdkeip.v2.CreatePublicipBandwidthOption`
        """
        self._bandwidth = bandwidth

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreatePublicipRequestBody.

        企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。  创建弹性公网IP时，给弹性公网IP绑定企业项目ID。  不指定该参数时，默认值是 0

        :return: The enterprise_project_id of this CreatePublicipRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreatePublicipRequestBody.

        企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。  创建弹性公网IP时，给弹性公网IP绑定企业项目ID。  不指定该参数时，默认值是 0

        :param enterprise_project_id: The enterprise_project_id of this CreatePublicipRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def publicip(self):
        r"""Gets the publicip of this CreatePublicipRequestBody.

        :return: The publicip of this CreatePublicipRequestBody.
        :rtype: :class:`huaweicloudsdkeip.v2.CreatePublicipOption`
        """
        return self._publicip

    @publicip.setter
    def publicip(self, publicip):
        r"""Sets the publicip of this CreatePublicipRequestBody.

        :param publicip: The publicip of this CreatePublicipRequestBody.
        :type publicip: :class:`huaweicloudsdkeip.v2.CreatePublicipOption`
        """
        self._publicip = publicip

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
        if not isinstance(other, CreatePublicipRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
