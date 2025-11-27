# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRecordSetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_zone_project_id': 'str',
        'x_zone_id': 'str',
        'body': 'list[CreateRecordSetRequestBody]'
    }

    attribute_map = {
        'x_zone_project_id': 'X-Zone-Project-ID',
        'x_zone_id': 'X-Zone-ID',
        'body': 'body'
    }

    def __init__(self, x_zone_project_id=None, x_zone_id=None, body=None):
        r"""CreateRecordSetRequest

        The model defined in huaweicloud sdk

        :param x_zone_project_id: 项目ID
        :type x_zone_project_id: str
        :param x_zone_id: DNS区域ID
        :type x_zone_id: str
        :param body: Body of the CreateRecordSetRequest
        :type body: list[:class:`huaweicloudsdkucs.v1.CreateRecordSetRequestBody`]
        """
        
        

        self._x_zone_project_id = None
        self._x_zone_id = None
        self._body = None
        self.discriminator = None

        self.x_zone_project_id = x_zone_project_id
        self.x_zone_id = x_zone_id
        if body is not None:
            self.body = body

    @property
    def x_zone_project_id(self):
        r"""Gets the x_zone_project_id of this CreateRecordSetRequest.

        项目ID

        :return: The x_zone_project_id of this CreateRecordSetRequest.
        :rtype: str
        """
        return self._x_zone_project_id

    @x_zone_project_id.setter
    def x_zone_project_id(self, x_zone_project_id):
        r"""Sets the x_zone_project_id of this CreateRecordSetRequest.

        项目ID

        :param x_zone_project_id: The x_zone_project_id of this CreateRecordSetRequest.
        :type x_zone_project_id: str
        """
        self._x_zone_project_id = x_zone_project_id

    @property
    def x_zone_id(self):
        r"""Gets the x_zone_id of this CreateRecordSetRequest.

        DNS区域ID

        :return: The x_zone_id of this CreateRecordSetRequest.
        :rtype: str
        """
        return self._x_zone_id

    @x_zone_id.setter
    def x_zone_id(self, x_zone_id):
        r"""Sets the x_zone_id of this CreateRecordSetRequest.

        DNS区域ID

        :param x_zone_id: The x_zone_id of this CreateRecordSetRequest.
        :type x_zone_id: str
        """
        self._x_zone_id = x_zone_id

    @property
    def body(self):
        r"""Gets the body of this CreateRecordSetRequest.

        :return: The body of this CreateRecordSetRequest.
        :rtype: list[:class:`huaweicloudsdkucs.v1.CreateRecordSetRequestBody`]
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateRecordSetRequest.

        :param body: The body of this CreateRecordSetRequest.
        :type body: list[:class:`huaweicloudsdkucs.v1.CreateRecordSetRequestBody`]
        """
        self._body = body

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateRecordSetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
