# coding: utf-8

import pprint
import re

import six





class BatchUpdateMembersRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'images': 'list[str]',
        'project_id': 'str',
        'status': 'str',
        'vault_id': 'str'
    }

    attribute_map = {
        'images': 'images',
        'project_id': 'project_id',
        'status': 'status',
        'vault_id': 'vault_id'
    }

    def __init__(self, images=None, project_id=None, status=None, vault_id=None):
        """BatchUpdateMembersRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._images = None
        self._project_id = None
        self._status = None
        self._vault_id = None
        self.discriminator = None

        self.images = images
        self.project_id = project_id
        self.status = status
        if vault_id is not None:
            self.vault_id = vault_id

    @property
    def images(self):
        """Gets the images of this BatchUpdateMembersRequestBody.

        镜像ID列表。

        :return: The images of this BatchUpdateMembersRequestBody.
        :rtype: list[str]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this BatchUpdateMembersRequestBody.

        镜像ID列表。

        :param images: The images of this BatchUpdateMembersRequestBody.
        :type: list[str]
        """
        self._images = images

    @property
    def project_id(self):
        """Gets the project_id of this BatchUpdateMembersRequestBody.

        项目ID。

        :return: The project_id of this BatchUpdateMembersRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BatchUpdateMembersRequestBody.

        项目ID。

        :param project_id: The project_id of this BatchUpdateMembersRequestBody.
        :type: str
        """
        self._project_id = project_id

    @property
    def status(self):
        """Gets the status of this BatchUpdateMembersRequestBody.

        镜像成员的状态。 取值如下： accepted：表示接受共享镜像。接受后，该镜像在用户镜像列表中可见，用户可以使用该镜像创建云服务器。 rejected：表示拒绝共享镜像。拒绝后，该镜像在用户镜像列表中不可见，但是，用户仍然可以使用该镜像创建云服务器。

        :return: The status of this BatchUpdateMembersRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BatchUpdateMembersRequestBody.

        镜像成员的状态。 取值如下： accepted：表示接受共享镜像。接受后，该镜像在用户镜像列表中可见，用户可以使用该镜像创建云服务器。 rejected：表示拒绝共享镜像。拒绝后，该镜像在用户镜像列表中不可见，但是，用户仍然可以使用该镜像创建云服务器。

        :param status: The status of this BatchUpdateMembersRequestBody.
        :type: str
        """
        self._status = status

    @property
    def vault_id(self):
        """Gets the vault_id of this BatchUpdateMembersRequestBody.

        存储库ID。 如果是通过CBR创建的整机镜像，则在接受该共享镜像时，为必选参数，需传入该值。

        :return: The vault_id of this BatchUpdateMembersRequestBody.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this BatchUpdateMembersRequestBody.

        存储库ID。 如果是通过CBR创建的整机镜像，则在接受该共享镜像时，为必选参数，需传入该值。

        :param vault_id: The vault_id of this BatchUpdateMembersRequestBody.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchUpdateMembersRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
