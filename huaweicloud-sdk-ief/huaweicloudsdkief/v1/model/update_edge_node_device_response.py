# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEdgeNodeDeviceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'delete_connector': 'bool',
        'deploy_connector': 'bool',
        'deployment_id': 'str',
        'update_devices': 'NodeDevice'
    }

    attribute_map = {
        'delete_connector': 'delete_connector',
        'deploy_connector': 'deploy_connector',
        'deployment_id': 'deployment_id',
        'update_devices': 'update_devices'
    }

    def __init__(self, delete_connector=None, deploy_connector=None, deployment_id=None, update_devices=None):
        """UpdateEdgeNodeDeviceResponse

        The model defined in huaweicloud sdk

        :param delete_connector: 工业终端设备预留字段
        :type delete_connector: bool
        :param deploy_connector: 工业终端设备预留字段
        :type deploy_connector: bool
        :param deployment_id: 工业终端设备预留字段
        :type deployment_id: str
        :param update_devices: 
        :type update_devices: :class:`huaweicloudsdkief.v1.NodeDevice`
        """
        
        super(UpdateEdgeNodeDeviceResponse, self).__init__()

        self._delete_connector = None
        self._deploy_connector = None
        self._deployment_id = None
        self._update_devices = None
        self.discriminator = None

        if delete_connector is not None:
            self.delete_connector = delete_connector
        if deploy_connector is not None:
            self.deploy_connector = deploy_connector
        if deployment_id is not None:
            self.deployment_id = deployment_id
        if update_devices is not None:
            self.update_devices = update_devices

    @property
    def delete_connector(self):
        """Gets the delete_connector of this UpdateEdgeNodeDeviceResponse.

        工业终端设备预留字段

        :return: The delete_connector of this UpdateEdgeNodeDeviceResponse.
        :rtype: bool
        """
        return self._delete_connector

    @delete_connector.setter
    def delete_connector(self, delete_connector):
        """Sets the delete_connector of this UpdateEdgeNodeDeviceResponse.

        工业终端设备预留字段

        :param delete_connector: The delete_connector of this UpdateEdgeNodeDeviceResponse.
        :type delete_connector: bool
        """
        self._delete_connector = delete_connector

    @property
    def deploy_connector(self):
        """Gets the deploy_connector of this UpdateEdgeNodeDeviceResponse.

        工业终端设备预留字段

        :return: The deploy_connector of this UpdateEdgeNodeDeviceResponse.
        :rtype: bool
        """
        return self._deploy_connector

    @deploy_connector.setter
    def deploy_connector(self, deploy_connector):
        """Sets the deploy_connector of this UpdateEdgeNodeDeviceResponse.

        工业终端设备预留字段

        :param deploy_connector: The deploy_connector of this UpdateEdgeNodeDeviceResponse.
        :type deploy_connector: bool
        """
        self._deploy_connector = deploy_connector

    @property
    def deployment_id(self):
        """Gets the deployment_id of this UpdateEdgeNodeDeviceResponse.

        工业终端设备预留字段

        :return: The deployment_id of this UpdateEdgeNodeDeviceResponse.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """Sets the deployment_id of this UpdateEdgeNodeDeviceResponse.

        工业终端设备预留字段

        :param deployment_id: The deployment_id of this UpdateEdgeNodeDeviceResponse.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

    @property
    def update_devices(self):
        """Gets the update_devices of this UpdateEdgeNodeDeviceResponse.


        :return: The update_devices of this UpdateEdgeNodeDeviceResponse.
        :rtype: :class:`huaweicloudsdkief.v1.NodeDevice`
        """
        return self._update_devices

    @update_devices.setter
    def update_devices(self, update_devices):
        """Sets the update_devices of this UpdateEdgeNodeDeviceResponse.


        :param update_devices: The update_devices of this UpdateEdgeNodeDeviceResponse.
        :type update_devices: :class:`huaweicloudsdkief.v1.NodeDevice`
        """
        self._update_devices = update_devices

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
        if not isinstance(other, UpdateEdgeNodeDeviceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
