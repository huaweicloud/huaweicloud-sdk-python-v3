# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrderAlertIncidentContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'title': 'str',
        'type_category': 'str',
        'evidence_list': 'list[str]',
        'note_list': 'list[str]',
        'attachment_list': 'list[str]',
        'incident_type': 'OrderAlertIncidentContentIncidentType',
        'description': 'str'
    }

    attribute_map = {
        'title': 'title',
        'type_category': 'type_category',
        'evidence_list': 'evidence_list',
        'note_list': 'note_list',
        'attachment_list': 'attachment_list',
        'incident_type': 'incident_type',
        'description': 'description'
    }

    def __init__(self, title=None, type_category=None, evidence_list=None, note_list=None, attachment_list=None, incident_type=None, description=None):
        """OrderAlertIncidentContent

        The model defined in huaweicloud sdk

        :param title: 事件名称
        :type title: str
        :param type_category: 事件类型
        :type type_category: str
        :param evidence_list: 证据列表
        :type evidence_list: list[str]
        :param note_list: 评论列表
        :type note_list: list[str]
        :param attachment_list: 附件列表
        :type attachment_list: list[str]
        :param incident_type: 
        :type incident_type: :class:`huaweicloudsdksa.v2.OrderAlertIncidentContentIncidentType`
        :param description: Id value
        :type description: str
        """
        
        

        self._title = None
        self._type_category = None
        self._evidence_list = None
        self._note_list = None
        self._attachment_list = None
        self._incident_type = None
        self._description = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if type_category is not None:
            self.type_category = type_category
        if evidence_list is not None:
            self.evidence_list = evidence_list
        if note_list is not None:
            self.note_list = note_list
        if attachment_list is not None:
            self.attachment_list = attachment_list
        if incident_type is not None:
            self.incident_type = incident_type
        if description is not None:
            self.description = description

    @property
    def title(self):
        """Gets the title of this OrderAlertIncidentContent.

        事件名称

        :return: The title of this OrderAlertIncidentContent.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this OrderAlertIncidentContent.

        事件名称

        :param title: The title of this OrderAlertIncidentContent.
        :type title: str
        """
        self._title = title

    @property
    def type_category(self):
        """Gets the type_category of this OrderAlertIncidentContent.

        事件类型

        :return: The type_category of this OrderAlertIncidentContent.
        :rtype: str
        """
        return self._type_category

    @type_category.setter
    def type_category(self, type_category):
        """Sets the type_category of this OrderAlertIncidentContent.

        事件类型

        :param type_category: The type_category of this OrderAlertIncidentContent.
        :type type_category: str
        """
        self._type_category = type_category

    @property
    def evidence_list(self):
        """Gets the evidence_list of this OrderAlertIncidentContent.

        证据列表

        :return: The evidence_list of this OrderAlertIncidentContent.
        :rtype: list[str]
        """
        return self._evidence_list

    @evidence_list.setter
    def evidence_list(self, evidence_list):
        """Sets the evidence_list of this OrderAlertIncidentContent.

        证据列表

        :param evidence_list: The evidence_list of this OrderAlertIncidentContent.
        :type evidence_list: list[str]
        """
        self._evidence_list = evidence_list

    @property
    def note_list(self):
        """Gets the note_list of this OrderAlertIncidentContent.

        评论列表

        :return: The note_list of this OrderAlertIncidentContent.
        :rtype: list[str]
        """
        return self._note_list

    @note_list.setter
    def note_list(self, note_list):
        """Sets the note_list of this OrderAlertIncidentContent.

        评论列表

        :param note_list: The note_list of this OrderAlertIncidentContent.
        :type note_list: list[str]
        """
        self._note_list = note_list

    @property
    def attachment_list(self):
        """Gets the attachment_list of this OrderAlertIncidentContent.

        附件列表

        :return: The attachment_list of this OrderAlertIncidentContent.
        :rtype: list[str]
        """
        return self._attachment_list

    @attachment_list.setter
    def attachment_list(self, attachment_list):
        """Sets the attachment_list of this OrderAlertIncidentContent.

        附件列表

        :param attachment_list: The attachment_list of this OrderAlertIncidentContent.
        :type attachment_list: list[str]
        """
        self._attachment_list = attachment_list

    @property
    def incident_type(self):
        """Gets the incident_type of this OrderAlertIncidentContent.

        :return: The incident_type of this OrderAlertIncidentContent.
        :rtype: :class:`huaweicloudsdksa.v2.OrderAlertIncidentContentIncidentType`
        """
        return self._incident_type

    @incident_type.setter
    def incident_type(self, incident_type):
        """Sets the incident_type of this OrderAlertIncidentContent.

        :param incident_type: The incident_type of this OrderAlertIncidentContent.
        :type incident_type: :class:`huaweicloudsdksa.v2.OrderAlertIncidentContentIncidentType`
        """
        self._incident_type = incident_type

    @property
    def description(self):
        """Gets the description of this OrderAlertIncidentContent.

        Id value

        :return: The description of this OrderAlertIncidentContent.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OrderAlertIncidentContent.

        Id value

        :param description: The description of this OrderAlertIncidentContent.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, OrderAlertIncidentContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
