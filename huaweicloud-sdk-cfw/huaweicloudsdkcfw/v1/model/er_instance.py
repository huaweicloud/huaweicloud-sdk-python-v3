# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ErInstance:

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
        'name': 'str',
        'project_id': 'str',
        'attachment_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'attachment_id': 'attachment_id'
    }

    def __init__(self, id=None, name=None, project_id=None, attachment_id=None):
        r"""ErInstance

        The model defined in huaweicloud sdk

        :param id: ER ID，创建ER时产生的ID
        :type id: str
        :param name: ER名称
        :type name: str
        :param project_id: 项目ID, 可以从调API处获取，也可以从控制台获取。[项目ID获取方式](cfw_02_0015.xml)
        :type project_id: str
        :param attachment_id: 企业路由器连接id，该连接用于连接防火墙和企业路由器，此字段可在通过id在ER界面查询指定er后在管理连接界面查询连接了解连接具体情况。
        :type attachment_id: str
        """
        
        

        self._id = None
        self._name = None
        self._project_id = None
        self._attachment_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if attachment_id is not None:
            self.attachment_id = attachment_id

    @property
    def id(self):
        r"""Gets the id of this ErInstance.

        ER ID，创建ER时产生的ID

        :return: The id of this ErInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ErInstance.

        ER ID，创建ER时产生的ID

        :param id: The id of this ErInstance.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ErInstance.

        ER名称

        :return: The name of this ErInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ErInstance.

        ER名称

        :param name: The name of this ErInstance.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this ErInstance.

        项目ID, 可以从调API处获取，也可以从控制台获取。[项目ID获取方式](cfw_02_0015.xml)

        :return: The project_id of this ErInstance.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ErInstance.

        项目ID, 可以从调API处获取，也可以从控制台获取。[项目ID获取方式](cfw_02_0015.xml)

        :param project_id: The project_id of this ErInstance.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def attachment_id(self):
        r"""Gets the attachment_id of this ErInstance.

        企业路由器连接id，该连接用于连接防火墙和企业路由器，此字段可在通过id在ER界面查询指定er后在管理连接界面查询连接了解连接具体情况。

        :return: The attachment_id of this ErInstance.
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        r"""Sets the attachment_id of this ErInstance.

        企业路由器连接id，该连接用于连接防火墙和企业路由器，此字段可在通过id在ER界面查询指定er后在管理连接界面查询连接了解连接具体情况。

        :param attachment_id: The attachment_id of this ErInstance.
        :type attachment_id: str
        """
        self._attachment_id = attachment_id

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
        if not isinstance(other, ErInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
