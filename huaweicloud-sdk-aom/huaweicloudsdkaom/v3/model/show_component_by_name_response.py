# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowComponentByNameResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'str',
        'aom_id': 'str',
        'app_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'aom_id': 'aom_id',
        'app_id': 'app_id'
    }

    def __init__(self, name=None, id=None, aom_id=None, app_id=None):
        """ShowComponentByNameResponse

        The model defined in huaweicloud sdk

        :param name: 组件名称
        :type name: str
        :param id: 组件id
        :type id: str
        :param aom_id: aomId
        :type aom_id: str
        :param app_id: 应用id
        :type app_id: str
        """
        
        super(ShowComponentByNameResponse, self).__init__()

        self._name = None
        self._id = None
        self._aom_id = None
        self._app_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if aom_id is not None:
            self.aom_id = aom_id
        if app_id is not None:
            self.app_id = app_id

    @property
    def name(self):
        """Gets the name of this ShowComponentByNameResponse.

        组件名称

        :return: The name of this ShowComponentByNameResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowComponentByNameResponse.

        组件名称

        :param name: The name of this ShowComponentByNameResponse.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this ShowComponentByNameResponse.

        组件id

        :return: The id of this ShowComponentByNameResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowComponentByNameResponse.

        组件id

        :param id: The id of this ShowComponentByNameResponse.
        :type id: str
        """
        self._id = id

    @property
    def aom_id(self):
        """Gets the aom_id of this ShowComponentByNameResponse.

        aomId

        :return: The aom_id of this ShowComponentByNameResponse.
        :rtype: str
        """
        return self._aom_id

    @aom_id.setter
    def aom_id(self, aom_id):
        """Sets the aom_id of this ShowComponentByNameResponse.

        aomId

        :param aom_id: The aom_id of this ShowComponentByNameResponse.
        :type aom_id: str
        """
        self._aom_id = aom_id

    @property
    def app_id(self):
        """Gets the app_id of this ShowComponentByNameResponse.

        应用id

        :return: The app_id of this ShowComponentByNameResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ShowComponentByNameResponse.

        应用id

        :param app_id: The app_id of this ShowComponentByNameResponse.
        :type app_id: str
        """
        self._app_id = app_id

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
        if not isinstance(other, ShowComponentByNameResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
