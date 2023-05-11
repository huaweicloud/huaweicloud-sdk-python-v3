# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlanceUpdateImageMemberRequestBody:

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
        'vault_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'vault_id': 'vault_id'
    }

    def __init__(self, status=None, vault_id=None):
        """GlanceUpdateImageMemberRequestBody

        The model defined in huaweicloud sdk

        :param status: 镜像成员的状态。 取值如下： accepted：表示接受共享镜像。接受后，该镜像在用户镜像列表中可见，用户可以使用该镜像创建云服务器。 rejected：表示拒绝共享镜像。拒绝后，该镜像在用户镜像列表中不可见，但是，用户仍然可以使用该镜像创建云服务器。
        :type status: str
        :param vault_id: 存储库ID。 如果是CBR创建的整机镜像，则在接受该共享镜像时，为必选参数，需传入该值。 存储库ID可以从云备份服务控制台获取，或者参考《云备份接口参考》的“查询存储库列表”章节查询。
        :type vault_id: str
        """
        
        

        self._status = None
        self._vault_id = None
        self.discriminator = None

        self.status = status
        if vault_id is not None:
            self.vault_id = vault_id

    @property
    def status(self):
        """Gets the status of this GlanceUpdateImageMemberRequestBody.

        镜像成员的状态。 取值如下： accepted：表示接受共享镜像。接受后，该镜像在用户镜像列表中可见，用户可以使用该镜像创建云服务器。 rejected：表示拒绝共享镜像。拒绝后，该镜像在用户镜像列表中不可见，但是，用户仍然可以使用该镜像创建云服务器。

        :return: The status of this GlanceUpdateImageMemberRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GlanceUpdateImageMemberRequestBody.

        镜像成员的状态。 取值如下： accepted：表示接受共享镜像。接受后，该镜像在用户镜像列表中可见，用户可以使用该镜像创建云服务器。 rejected：表示拒绝共享镜像。拒绝后，该镜像在用户镜像列表中不可见，但是，用户仍然可以使用该镜像创建云服务器。

        :param status: The status of this GlanceUpdateImageMemberRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def vault_id(self):
        """Gets the vault_id of this GlanceUpdateImageMemberRequestBody.

        存储库ID。 如果是CBR创建的整机镜像，则在接受该共享镜像时，为必选参数，需传入该值。 存储库ID可以从云备份服务控制台获取，或者参考《云备份接口参考》的“查询存储库列表”章节查询。

        :return: The vault_id of this GlanceUpdateImageMemberRequestBody.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this GlanceUpdateImageMemberRequestBody.

        存储库ID。 如果是CBR创建的整机镜像，则在接受该共享镜像时，为必选参数，需传入该值。 存储库ID可以从云备份服务控制台获取，或者参考《云备份接口参考》的“查询存储库列表”章节查询。

        :param vault_id: The vault_id of this GlanceUpdateImageMemberRequestBody.
        :type vault_id: str
        """
        self._vault_id = vault_id

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
        if not isinstance(other, GlanceUpdateImageMemberRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
