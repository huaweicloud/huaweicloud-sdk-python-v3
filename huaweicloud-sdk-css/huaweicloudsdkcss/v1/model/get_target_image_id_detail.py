# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetTargetImageIdDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'display_name': 'str',
        'image_desc': 'str',
        'datastore_type': 'str',
        'datastore_version': 'str',
        'priority': 'int'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'displayName',
        'image_desc': 'imageDesc',
        'datastore_type': 'datastoreType',
        'datastore_version': 'datastoreVersion',
        'priority': 'priority'
    }

    def __init__(self, id=None, display_name=None, image_desc=None, datastore_type=None, datastore_version=None, priority=None):
        r"""GetTargetImageIdDetail

        The model defined in huaweicloud sdk

        :param id: 可以升级的目标镜像ID。
        :type id: str
        :param display_name: 可以升级的目标镜像名称。
        :type display_name: str
        :param image_desc: 镜像描述信息。
        :type image_desc: str
        :param datastore_type: 镜像引擎类型。
        :type datastore_type: str
        :param datastore_version: 镜像引擎版本。
        :type datastore_version: str
        :param priority: 优先级。
        :type priority: int
        """
        
        

        self._id = None
        self._display_name = None
        self._image_desc = None
        self._datastore_type = None
        self._datastore_version = None
        self._priority = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if display_name is not None:
            self.display_name = display_name
        if image_desc is not None:
            self.image_desc = image_desc
        if datastore_type is not None:
            self.datastore_type = datastore_type
        if datastore_version is not None:
            self.datastore_version = datastore_version
        if priority is not None:
            self.priority = priority

    @property
    def id(self):
        r"""Gets the id of this GetTargetImageIdDetail.

        可以升级的目标镜像ID。

        :return: The id of this GetTargetImageIdDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GetTargetImageIdDetail.

        可以升级的目标镜像ID。

        :param id: The id of this GetTargetImageIdDetail.
        :type id: str
        """
        self._id = id

    @property
    def display_name(self):
        r"""Gets the display_name of this GetTargetImageIdDetail.

        可以升级的目标镜像名称。

        :return: The display_name of this GetTargetImageIdDetail.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this GetTargetImageIdDetail.

        可以升级的目标镜像名称。

        :param display_name: The display_name of this GetTargetImageIdDetail.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def image_desc(self):
        r"""Gets the image_desc of this GetTargetImageIdDetail.

        镜像描述信息。

        :return: The image_desc of this GetTargetImageIdDetail.
        :rtype: str
        """
        return self._image_desc

    @image_desc.setter
    def image_desc(self, image_desc):
        r"""Sets the image_desc of this GetTargetImageIdDetail.

        镜像描述信息。

        :param image_desc: The image_desc of this GetTargetImageIdDetail.
        :type image_desc: str
        """
        self._image_desc = image_desc

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this GetTargetImageIdDetail.

        镜像引擎类型。

        :return: The datastore_type of this GetTargetImageIdDetail.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this GetTargetImageIdDetail.

        镜像引擎类型。

        :param datastore_type: The datastore_type of this GetTargetImageIdDetail.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def datastore_version(self):
        r"""Gets the datastore_version of this GetTargetImageIdDetail.

        镜像引擎版本。

        :return: The datastore_version of this GetTargetImageIdDetail.
        :rtype: str
        """
        return self._datastore_version

    @datastore_version.setter
    def datastore_version(self, datastore_version):
        r"""Sets the datastore_version of this GetTargetImageIdDetail.

        镜像引擎版本。

        :param datastore_version: The datastore_version of this GetTargetImageIdDetail.
        :type datastore_version: str
        """
        self._datastore_version = datastore_version

    @property
    def priority(self):
        r"""Gets the priority of this GetTargetImageIdDetail.

        优先级。

        :return: The priority of this GetTargetImageIdDetail.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this GetTargetImageIdDetail.

        优先级。

        :param priority: The priority of this GetTargetImageIdDetail.
        :type priority: int
        """
        self._priority = priority

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
        if not isinstance(other, GetTargetImageIdDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
