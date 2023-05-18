# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckDisasterNameRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dr_name': 'str',
        'type': 'str',
        'standby_region': 'str',
        'standby_project_id': 'str'
    }

    attribute_map = {
        'dr_name': 'dr_name',
        'type': 'type',
        'standby_region': 'standby_region',
        'standby_project_id': 'standby_project_id'
    }

    def __init__(self, dr_name=None, type=None, standby_region=None, standby_project_id=None):
        """CheckDisasterNameRequest

        The model defined in huaweicloud sdk

        :param dr_name: 容灾名称
        :type dr_name: str
        :param type: 容灾类型
        :type type: str
        :param standby_region: 备集群所在region
        :type standby_region: str
        :param standby_project_id: 备集群所在项目ID
        :type standby_project_id: str
        """
        
        

        self._dr_name = None
        self._type = None
        self._standby_region = None
        self._standby_project_id = None
        self.discriminator = None

        self.dr_name = dr_name
        if type is not None:
            self.type = type
        if standby_region is not None:
            self.standby_region = standby_region
        if standby_project_id is not None:
            self.standby_project_id = standby_project_id

    @property
    def dr_name(self):
        """Gets the dr_name of this CheckDisasterNameRequest.

        容灾名称

        :return: The dr_name of this CheckDisasterNameRequest.
        :rtype: str
        """
        return self._dr_name

    @dr_name.setter
    def dr_name(self, dr_name):
        """Sets the dr_name of this CheckDisasterNameRequest.

        容灾名称

        :param dr_name: The dr_name of this CheckDisasterNameRequest.
        :type dr_name: str
        """
        self._dr_name = dr_name

    @property
    def type(self):
        """Gets the type of this CheckDisasterNameRequest.

        容灾类型

        :return: The type of this CheckDisasterNameRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CheckDisasterNameRequest.

        容灾类型

        :param type: The type of this CheckDisasterNameRequest.
        :type type: str
        """
        self._type = type

    @property
    def standby_region(self):
        """Gets the standby_region of this CheckDisasterNameRequest.

        备集群所在region

        :return: The standby_region of this CheckDisasterNameRequest.
        :rtype: str
        """
        return self._standby_region

    @standby_region.setter
    def standby_region(self, standby_region):
        """Sets the standby_region of this CheckDisasterNameRequest.

        备集群所在region

        :param standby_region: The standby_region of this CheckDisasterNameRequest.
        :type standby_region: str
        """
        self._standby_region = standby_region

    @property
    def standby_project_id(self):
        """Gets the standby_project_id of this CheckDisasterNameRequest.

        备集群所在项目ID

        :return: The standby_project_id of this CheckDisasterNameRequest.
        :rtype: str
        """
        return self._standby_project_id

    @standby_project_id.setter
    def standby_project_id(self, standby_project_id):
        """Sets the standby_project_id of this CheckDisasterNameRequest.

        备集群所在项目ID

        :param standby_project_id: The standby_project_id of this CheckDisasterNameRequest.
        :type standby_project_id: str
        """
        self._standby_project_id = standby_project_id

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
        if not isinstance(other, CheckDisasterNameRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
