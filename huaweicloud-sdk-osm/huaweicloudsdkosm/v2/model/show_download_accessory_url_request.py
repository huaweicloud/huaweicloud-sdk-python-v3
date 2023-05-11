# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDownloadAccessoryUrlRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'accessory_id': 'str',
        'relation_type': 'str',
        'relation_id': 'str',
        'incident_id': 'str'
    }

    attribute_map = {
        'accessory_id': 'accessory_id',
        'relation_type': 'relation_type',
        'relation_id': 'relation_id',
        'incident_id': 'incident_id'
    }

    def __init__(self, accessory_id=None, relation_type=None, relation_id=None, incident_id=None):
        """ShowDownloadAccessoryUrlRequest

        The model defined in huaweicloud sdk

        :param accessory_id: 附件id
        :type accessory_id: str
        :param relation_type: - DEFAULT:  - NO_RELATION:  - NOTIFICATION:  - INCIDENT:  - MESSAGE:  - INSPECTION:  - CONNECT:  
        :type relation_type: str
        :param relation_id: 关联id
        :type relation_id: str
        :param incident_id: 工单id
        :type incident_id: str
        """
        
        

        self._accessory_id = None
        self._relation_type = None
        self._relation_id = None
        self._incident_id = None
        self.discriminator = None

        self.accessory_id = accessory_id
        self.relation_type = relation_type
        if relation_id is not None:
            self.relation_id = relation_id
        if incident_id is not None:
            self.incident_id = incident_id

    @property
    def accessory_id(self):
        """Gets the accessory_id of this ShowDownloadAccessoryUrlRequest.

        附件id

        :return: The accessory_id of this ShowDownloadAccessoryUrlRequest.
        :rtype: str
        """
        return self._accessory_id

    @accessory_id.setter
    def accessory_id(self, accessory_id):
        """Sets the accessory_id of this ShowDownloadAccessoryUrlRequest.

        附件id

        :param accessory_id: The accessory_id of this ShowDownloadAccessoryUrlRequest.
        :type accessory_id: str
        """
        self._accessory_id = accessory_id

    @property
    def relation_type(self):
        """Gets the relation_type of this ShowDownloadAccessoryUrlRequest.

        - DEFAULT:  - NO_RELATION:  - NOTIFICATION:  - INCIDENT:  - MESSAGE:  - INSPECTION:  - CONNECT:  

        :return: The relation_type of this ShowDownloadAccessoryUrlRequest.
        :rtype: str
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        """Sets the relation_type of this ShowDownloadAccessoryUrlRequest.

        - DEFAULT:  - NO_RELATION:  - NOTIFICATION:  - INCIDENT:  - MESSAGE:  - INSPECTION:  - CONNECT:  

        :param relation_type: The relation_type of this ShowDownloadAccessoryUrlRequest.
        :type relation_type: str
        """
        self._relation_type = relation_type

    @property
    def relation_id(self):
        """Gets the relation_id of this ShowDownloadAccessoryUrlRequest.

        关联id

        :return: The relation_id of this ShowDownloadAccessoryUrlRequest.
        :rtype: str
        """
        return self._relation_id

    @relation_id.setter
    def relation_id(self, relation_id):
        """Sets the relation_id of this ShowDownloadAccessoryUrlRequest.

        关联id

        :param relation_id: The relation_id of this ShowDownloadAccessoryUrlRequest.
        :type relation_id: str
        """
        self._relation_id = relation_id

    @property
    def incident_id(self):
        """Gets the incident_id of this ShowDownloadAccessoryUrlRequest.

        工单id

        :return: The incident_id of this ShowDownloadAccessoryUrlRequest.
        :rtype: str
        """
        return self._incident_id

    @incident_id.setter
    def incident_id(self, incident_id):
        """Sets the incident_id of this ShowDownloadAccessoryUrlRequest.

        工单id

        :param incident_id: The incident_id of this ShowDownloadAccessoryUrlRequest.
        :type incident_id: str
        """
        self._incident_id = incident_id

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
        if not isinstance(other, ShowDownloadAccessoryUrlRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
