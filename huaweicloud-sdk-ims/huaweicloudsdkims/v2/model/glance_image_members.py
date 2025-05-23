# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlanceImageMembers:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'image_id': 'str',
        'member_id': 'str',
        'schema': 'str'
    }

    attribute_map = {
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'image_id': 'image_id',
        'member_id': 'member_id',
        'schema': 'schema'
    }

    def __init__(self, status=None, created_at=None, updated_at=None, image_id=None, member_id=None, schema=None):
        r"""GlanceImageMembers

        The model defined in huaweicloud sdk

        :param status: 共享状态。
        :type status: str
        :param created_at: 共享时间，格式为UTC时间。
        :type created_at: str
        :param updated_at: 更新时间，格式为UTC时间。
        :type updated_at: str
        :param image_id: 镜像ID。
        :type image_id: str
        :param member_id: 成员ID。
        :type member_id: str
        :param schema: 共享视图。
        :type schema: str
        """
        
        

        self._status = None
        self._created_at = None
        self._updated_at = None
        self._image_id = None
        self._member_id = None
        self._schema = None
        self.discriminator = None

        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        self.image_id = image_id
        self.member_id = member_id
        self.schema = schema

    @property
    def status(self):
        r"""Gets the status of this GlanceImageMembers.

        共享状态。

        :return: The status of this GlanceImageMembers.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this GlanceImageMembers.

        共享状态。

        :param status: The status of this GlanceImageMembers.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this GlanceImageMembers.

        共享时间，格式为UTC时间。

        :return: The created_at of this GlanceImageMembers.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this GlanceImageMembers.

        共享时间，格式为UTC时间。

        :param created_at: The created_at of this GlanceImageMembers.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this GlanceImageMembers.

        更新时间，格式为UTC时间。

        :return: The updated_at of this GlanceImageMembers.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this GlanceImageMembers.

        更新时间，格式为UTC时间。

        :param updated_at: The updated_at of this GlanceImageMembers.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def image_id(self):
        r"""Gets the image_id of this GlanceImageMembers.

        镜像ID。

        :return: The image_id of this GlanceImageMembers.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this GlanceImageMembers.

        镜像ID。

        :param image_id: The image_id of this GlanceImageMembers.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def member_id(self):
        r"""Gets the member_id of this GlanceImageMembers.

        成员ID。

        :return: The member_id of this GlanceImageMembers.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        r"""Sets the member_id of this GlanceImageMembers.

        成员ID。

        :param member_id: The member_id of this GlanceImageMembers.
        :type member_id: str
        """
        self._member_id = member_id

    @property
    def schema(self):
        r"""Gets the schema of this GlanceImageMembers.

        共享视图。

        :return: The schema of this GlanceImageMembers.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this GlanceImageMembers.

        共享视图。

        :param schema: The schema of this GlanceImageMembers.
        :type schema: str
        """
        self._schema = schema

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
        if not isinstance(other, GlanceImageMembers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
