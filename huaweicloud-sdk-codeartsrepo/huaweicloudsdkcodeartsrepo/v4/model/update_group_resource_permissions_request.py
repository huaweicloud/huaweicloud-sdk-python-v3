# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGroupResourcePermissionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'int',
        'resource_id': 'int',
        'body': 'UpdatePermissionBodyDto'
    }

    attribute_map = {
        'group_id': 'group_id',
        'resource_id': 'resource_id',
        'body': 'body'
    }

    def __init__(self, group_id=None, resource_id=None, body=None):
        r"""UpdateGroupResourcePermissionsRequest

        The model defined in huaweicloud sdk

        :param group_id: **参数解释：** 代码组id，代码组首页，Group ID后的数字Id **默认取值：** 不涉及。
        :type group_id: int
        :param resource_id: **参数解释：** 资源Id，通过获取代码组权限资源点列表获取的数据中的Id **默认取值：** 不涉及。
        :type resource_id: int
        :param body: Body of the UpdateGroupResourcePermissionsRequest
        :type body: :class:`huaweicloudsdkcodeartsrepo.v4.UpdatePermissionBodyDto`
        """
        
        

        self._group_id = None
        self._resource_id = None
        self._body = None
        self.discriminator = None

        self.group_id = group_id
        self.resource_id = resource_id
        if body is not None:
            self.body = body

    @property
    def group_id(self):
        r"""Gets the group_id of this UpdateGroupResourcePermissionsRequest.

        **参数解释：** 代码组id，代码组首页，Group ID后的数字Id **默认取值：** 不涉及。

        :return: The group_id of this UpdateGroupResourcePermissionsRequest.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this UpdateGroupResourcePermissionsRequest.

        **参数解释：** 代码组id，代码组首页，Group ID后的数字Id **默认取值：** 不涉及。

        :param group_id: The group_id of this UpdateGroupResourcePermissionsRequest.
        :type group_id: int
        """
        self._group_id = group_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this UpdateGroupResourcePermissionsRequest.

        **参数解释：** 资源Id，通过获取代码组权限资源点列表获取的数据中的Id **默认取值：** 不涉及。

        :return: The resource_id of this UpdateGroupResourcePermissionsRequest.
        :rtype: int
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this UpdateGroupResourcePermissionsRequest.

        **参数解释：** 资源Id，通过获取代码组权限资源点列表获取的数据中的Id **默认取值：** 不涉及。

        :param resource_id: The resource_id of this UpdateGroupResourcePermissionsRequest.
        :type resource_id: int
        """
        self._resource_id = resource_id

    @property
    def body(self):
        r"""Gets the body of this UpdateGroupResourcePermissionsRequest.

        :return: The body of this UpdateGroupResourcePermissionsRequest.
        :rtype: :class:`huaweicloudsdkcodeartsrepo.v4.UpdatePermissionBodyDto`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateGroupResourcePermissionsRequest.

        :param body: The body of this UpdateGroupResourcePermissionsRequest.
        :type body: :class:`huaweicloudsdkcodeartsrepo.v4.UpdatePermissionBodyDto`
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
        if not isinstance(other, UpdateGroupResourcePermissionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
