# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTagRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fw_instance_id': 'str',
        'body': 'DeleteTagsDto'
    }

    attribute_map = {
        'fw_instance_id': 'fw_instance_id',
        'body': 'body'
    }

    def __init__(self, fw_instance_id=None, body=None):
        r"""DeleteTagRequest

        The model defined in huaweicloud sdk

        :param fw_instance_id: 防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取
        :type fw_instance_id: str
        :param body: Body of the DeleteTagRequest
        :type body: :class:`huaweicloudsdkcfw.v1.DeleteTagsDto`
        """
        
        

        self._fw_instance_id = None
        self._body = None
        self.discriminator = None

        self.fw_instance_id = fw_instance_id
        if body is not None:
            self.body = body

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this DeleteTagRequest.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :return: The fw_instance_id of this DeleteTagRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this DeleteTagRequest.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :param fw_instance_id: The fw_instance_id of this DeleteTagRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def body(self):
        r"""Gets the body of this DeleteTagRequest.

        :return: The body of this DeleteTagRequest.
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteTagsDto`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this DeleteTagRequest.

        :param body: The body of this DeleteTagRequest.
        :type body: :class:`huaweicloudsdkcfw.v1.DeleteTagsDto`
        """
        self._body = body

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
        if not isinstance(other, DeleteTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
