# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageMembersView:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'int',
        'update_time': 'int',
        'image_id': 'str',
        'member_id': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'update_time': 'update_time',
        'image_id': 'image_id',
        'member_id': 'member_id'
    }

    def __init__(self, create_time=None, update_time=None, image_id=None, member_id=None):
        """ListImageMembersView

        The model defined in huaweicloud sdk

        :param create_time: 共享时间
        :type create_time: int
        :param update_time: 更新时间
        :type update_time: int
        :param image_id: 镜像ID
        :type image_id: str
        :param member_id: 被共享账号的PROJECT_ID
        :type member_id: str
        """
        
        

        self._create_time = None
        self._update_time = None
        self._image_id = None
        self._member_id = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if image_id is not None:
            self.image_id = image_id
        if member_id is not None:
            self.member_id = member_id

    @property
    def create_time(self):
        """Gets the create_time of this ListImageMembersView.

        共享时间

        :return: The create_time of this ListImageMembersView.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ListImageMembersView.

        共享时间

        :param create_time: The create_time of this ListImageMembersView.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ListImageMembersView.

        更新时间

        :return: The update_time of this ListImageMembersView.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ListImageMembersView.

        更新时间

        :param update_time: The update_time of this ListImageMembersView.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def image_id(self):
        """Gets the image_id of this ListImageMembersView.

        镜像ID

        :return: The image_id of this ListImageMembersView.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ListImageMembersView.

        镜像ID

        :param image_id: The image_id of this ListImageMembersView.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def member_id(self):
        """Gets the member_id of this ListImageMembersView.

        被共享账号的PROJECT_ID

        :return: The member_id of this ListImageMembersView.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """Sets the member_id of this ListImageMembersView.

        被共享账号的PROJECT_ID

        :param member_id: The member_id of this ListImageMembersView.
        :type member_id: str
        """
        self._member_id = member_id

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
        if not isinstance(other, ListImageMembersView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
